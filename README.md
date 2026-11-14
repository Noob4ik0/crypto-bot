# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 48**

| Date | Headline |
|------|----------|
| 2026-11-13 | JPMorgan’s Bitcoin and Crypto-Linked Holdings Approach $1 Billion… |
| 2026-11-14 | Adam Back makes case for simpler security as Blockstream launches Bitcoin custod… |
| 2026-11-14 | Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out… |
| 2026-11-14 | Bitcoin Hits 12-Week Low as Fed Rate Fears Undo Most of Summer Rally… |
| 2026-11-14 | Bitcoin ETFs shed $2.35B in 2 weeks, BlackRock’s losing streak hits 11… |

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
*README auto-updated: 2026-11-14 13:00 UTC*
