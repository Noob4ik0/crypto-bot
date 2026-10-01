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
| 2026-10-01 | SlowMist traces Bitget hack activity to Aug. 31 zero-day exploit… |
| 2026-10-01 | MetaMask exits Ethereum validators amid undisclosed security incident… |
| 2026-10-01 | CFTC Sends White House New Rules to Cement Its Grip on Prediction Markets… |
| 2026-10-01 | Crypto hacks top $768M in September, worst month of 2026… |
| 2026-10-01 | Bitcoin ETFs draw $6.3B in Q3 as BTC price rises nearly 43%… |

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
*README auto-updated: 2026-10-01 13:00 UTC*
