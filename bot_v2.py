#!/usr/bin/env python3
"""CryptoBot v2 — crypto news monitor & auto-poster to Farcaster (only important news)"""

import os
import re
import json
import time
import hashlib
import logging
import feedparser
import requests
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

# ── Bootstrap ─────────────────────────────────────────────────────────────────
load_dotenv()

BOT_DIR  = Path(__file__).parent
LOG_FILE = BOT_DIR / "bot.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(LOG_FILE)],
)
log = logging.getLogger(__name__)

# ── Settings ──────────────────────────────────────────────────────────────────
MAX_POSTS_PER_CYCLE = 1        # максимум 1 пост за цикл
MONITOR_MIN         = 30       # проверка раз в 30 минут
MIN_IMPORTANCE      = 8        # минимальная оценка важности (1-10) для публикации
SEEN_TTL_DAYS       = 7        # хранить хеши 7 дней
MIN_HOURS_BETWEEN   = 2        # минимум 2 часа между постами

SEEN_FILE  = BOT_DIR / "seen_hashes.json"
STATE_FILE = BOT_DIR / "state.json"

# ── Keywords (первичный фильтр) ───────────────────────────────────────────────
WORD_KEYWORDS = {
    "btc", "eth", "bnb", "xrp", "sol",
    "ada", "doge", "avax", "dot", "matic",
    "nft", "l2",
}

PHRASE_KEYWORDS = {
    "bitcoin", "ethereum", "binance", "ripple", "solana",
    "cardano", "dogecoin", "avalanche", "polkadot", "polygon",
    "airdrop", "token distribution", "retroactive drop", "claim tokens",
    "vc funding", "venture capital", "funding round", "raises",
    "seed round", "series a", "series b",
    "defi", "decentralized finance", "yield farming", "liquidity pool", "tvl",
    "layer2", "layer 2", "rollup", "zk rollup", "zero knowledge",
    "regulation", "sec crypto", "cftc", "crypto legislation", "crypto bill",
    "cbdc", "crypto ban", "mica regulation", "crypto tax",
    "crypto", "blockchain", "web3", "token launch", "mainnet launch",
    "hack", "exploit", "hacked", "stolen", "breach", "vulnerability",
    "etf", "blackrock", "fidelity", "institutional", "spot bitcoin",
    "fed", "interest rate", "inflation", "macro",
    "halving", "merge", "upgrade", "hard fork",
}

# ── RSS Feeds ─────────────────────────────────────────────────────────────────
RSS_FEEDS = {
    "CoinDesk":      "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "CoinTelegraph": "https://cointelegraph.com/rss",
    "Decrypt":       "https://decrypt.co/feed",
    "TheBlock":      "https://www.theblockcrypto.com/rss.xml",
}

# ── OpenRouter (AI) ───────────────────────────────────────────────────────────
OR_KEY    = os.getenv("OPENROUTER_API_KEY")
OR_MODELS = [
    "google/gemma-4-26b-a4b-it:free",
    "google/gemma-4-31b-it:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
]


def score_importance(title: str) -> int:
    """Просит AI оценить важность новости от 1 до 10. Возвращает 0 при ошибке."""
    if not OR_KEY:
        log.warning("[AI] OPENROUTER_API_KEY not set — skipping AI filter")
        return 5

    prompt = f"""Rate the importance of this crypto news headline from 1 to 10.

Scale:
9-10 = Market-moving event: major hack/exploit (>$10M), ETF approval, government ban, exchange collapse, major protocol exploit
7-8  = Significant: major funding round (>$50M), mainnet launch of top project, Fed/macro decision, major partnership
5-6  = Moderate: regular funding rounds, protocol upgrades, new features
3-4  = Minor: small updates, opinion pieces, minor partnerships
1-2  = Not newsworthy: price commentary, minor news, speculation

Headline: "{title}"

Reply with ONLY a single integer (1-10), nothing else."""

    for model in OR_MODELS:
        try:
            r = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {OR_KEY}", "Content-Type": "application/json"},
                json={"model": model, "messages": [{"role": "user", "content": prompt}], "max_tokens": 5},
                timeout=20,
            )
            r.raise_for_status()
            data = r.json()
            if "choices" not in data or not data["choices"]:
                log.warning(f"[AI:{model}] empty response")
                continue
            text = data["choices"][0]["message"]["content"].strip()
            match = re.search(r'\d+', text)
            if not match:
                log.warning(f"[AI:{model}] no score in: {text[:30]}")
                continue
            score = max(1, min(10, int(match.group())))
            log.info(f"[AI:{model.split('/')[-1]}] score={score} | {title[:70]}")
            return score
        except requests.exceptions.Timeout:
            log.warning(f"[AI:{model}] timeout")
            continue
        except Exception as e:
            log.warning(f"[AI:{model}] error: {e}")
            continue

    log.warning("[AI] all models failed — skipping")
    return 0


# ── Deduplication ─────────────────────────────────────────────────────────────
def load_seen() -> dict:
    if SEEN_FILE.exists():
        try:
            return json.loads(SEEN_FILE.read_text())
        except Exception:
            pass
    return {}


def save_seen(seen: dict):
    # Чистим старые записи (старше SEEN_TTL_DAYS)
    cutoff = (datetime.now() - timedelta(days=SEEN_TTL_DAYS)).isoformat()
    cleaned = {h: ts for h, ts in seen.items() if ts >= cutoff}
    SEEN_FILE.write_text(json.dumps(cleaned, indent=2))


def md5(text: str) -> str:
    return hashlib.md5(text.strip().lower().encode()).hexdigest()


# ── State (последний пост) ────────────────────────────────────────────────────
def load_last_posted() -> datetime | None:
    if STATE_FILE.exists():
        try:
            data = json.loads(STATE_FILE.read_text())
            return datetime.fromisoformat(data["last_posted"])
        except Exception:
            pass
    return None


def save_last_posted():
    STATE_FILE.write_text(json.dumps({"last_posted": datetime.now().isoformat()}))


# ── Relevance matching ────────────────────────────────────────────────────────
_WORD_PATTERNS = {kw: re.compile(r"\b" + re.escape(kw) + r"\b") for kw in WORD_KEYWORDS}


def is_relevant(title: str) -> bool:
    low = title.lower()
    for kw in PHRASE_KEYWORDS:
        if kw in low:
            return True
    for kw, pattern in _WORD_PATTERNS.items():
        if pattern.search(low):
            return True
    return False


# ── News fetching ─────────────────────────────────────────────────────────────
def fetch_rss() -> list:
    items = []
    for name, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:15]:
                title = entry.get("title", "").strip()
                link  = entry.get("link", "")
                if title:
                    items.append({"title": title, "url": link, "source": name})
        except Exception as e:
            log.error(f"RSS fetch error ({name}): {e}")
    return items


# ── Post formatting ───────────────────────────────────────────────────────────
def format_cast(title: str, url: str) -> str:
    base = f"{title}\n\n{url}"
    if len(base) <= 320:
        return base
    return title[:290] + "…\n\n" + url


# ── Farcaster (Neynar) ────────────────────────────────────────────────────────
def post_farcaster(text: str) -> bool:
    api_key = os.getenv("FARCASTER_NEYNAR_API_KEY")
    signer  = os.getenv("FARCASTER_SIGNER_UUID")
    if not api_key or not signer:
        log.warning("[Farcaster] credentials not set — skipping")
        return False
    try:
        r = requests.post(
            "https://api.neynar.com/v2/farcaster/cast",
            headers={"api_key": api_key, "Content-Type": "application/json"},
            json={"signer_uuid": signer, "text": text},
            timeout=10,
        )
        r.raise_for_status()
        log.info(f"[Farcaster] posted: {text[:80]}…")
        return True
    except Exception as e:
        log.error(f"[Farcaster] post error: {e}")
        return False


# ── Main cycle ────────────────────────────────────────────────────────────────
def monitor_cycle():
    log.info("══ Monitor cycle started ══")

    # Проверяем паузу между постами
    last_posted = load_last_posted()
    if last_posted:
        elapsed_h = (datetime.now() - last_posted).total_seconds() / 3600
        if elapsed_h < MIN_HOURS_BETWEEN:
            log.info(f"[Cooldown] last post {elapsed_h:.1f}h ago — min {MIN_HOURS_BETWEEN}h, skipping")
            return

    seen = load_seen()
    news = fetch_rss()

    # Первичный фильтр по ключевым словам
    candidates = [
        n for n in news
        if is_relevant(n["title"]) and md5(n["title"]) not in seen
    ]
    log.info(f"Total: {len(news)} | Relevant & new: {len(candidates)}")

    posted = 0
    for item in candidates:
        if posted >= MAX_POSTS_PER_CYCLE:
            break

        title = item["title"]

        # AI-оценка важности
        score = score_importance(title)
        if score < MIN_IMPORTANCE:
            log.info(f"[SKIP score={score}<{MIN_IMPORTANCE}] {title[:80]}")
            seen[md5(title)] = datetime.now().isoformat()
            save_seen(seen)
            continue

        # Публикуем
        log.info(f"[POST score={score}] [{item['source']}] {title[:80]}")
        cast = format_cast(title, item["url"])
        ok   = post_farcaster(cast)

        seen[md5(title)] = datetime.now().isoformat()
        save_seen(seen)

        if ok:
            posted += 1
            save_last_posted()

    log.info(f"══ Cycle done: {posted}/{MAX_POSTS_PER_CYCLE} posts ══")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    log.info("CryptoBot v2 starting…")
    log.info(f"Settings: check every {MONITOR_MIN}m | min importance {MIN_IMPORTANCE}/10 | min {MIN_HOURS_BETWEEN}h between posts")

    # Чистим старые seen_hashes при старте
    seen = load_seen()
    if isinstance(seen, list):  # старый формат (список хешей)
        seen = {}
    cutoff = (datetime.now() - timedelta(days=SEEN_TTL_DAYS)).isoformat()
    seen = {h: ts for h, ts in seen.items() if ts >= cutoff}
    SEEN_FILE.write_text(json.dumps(seen, indent=2))
    log.info(f"Seen cache: {len(seen)} hashes (cleaned to last {SEEN_TTL_DAYS} days)")

    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(monitor_cycle, "interval", minutes=MONITOR_MIN, id="monitor")

    monitor_cycle()  # сразу при старте

    log.info(f"Scheduler active — checking every {MONITOR_MIN} min")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        log.info("CryptoBot v2 stopped")
