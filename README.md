# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 56**

| Date | Headline |
|------|----------|
| 2026-07-28 | Crypto’s favorite $90 trillion trading product is coming to Wall Street, but big… |
| 2026-07-28 | Hong Kong crypto giant HashKey merges regional exchange into one… |
| 2026-07-28 | Prediction Market Traders Brace for Surprise Fed Rate Hike… |
| 2026-07-28 | Fanatics Buys CFTC-Registered Exchange in Prediction Markets Land Grab… |
| 2026-07-28 | Inside the CME and CFTC’s battle over onchain perpetual futures… |

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
*README auto-updated: 2026-07-28 13:00 UTC*
