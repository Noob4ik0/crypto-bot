# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 49**

| Date | Headline |
|------|----------|
| 2026-09-26 | Another appeals court rules against prediction market provider Kalshi, says spor… |
| 2026-09-26 | Bitget clarifies $388M in assets affected by security breach… |
| 2026-09-26 | KelpDAO sues LayerZero, CEO over $292M rsETH bridge exploit… |
| 2026-09-26 | Bitcoin ETF inflows slow to $191M as six-day streak reaches $2.8B… |
| 2026-09-26 | Bitget Hack Losses Climb to $387M: Here’s What Happened, and Why North Korea Is … |

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # fill in your keys
python bot_v2.py
```

## Environment variables

See `.env.example` for required keys:
- `FARCASTER_NEYNAR_API_KEY` — Neynar API key
- `FARCASTER_SIGNER_UUID` — Farcaster signer UUID
- `OPENROUTER_API_KEY` — OpenRouter API key (free tier works)

---
*README auto-updated: 2026-09-26 13:00 UTC*
