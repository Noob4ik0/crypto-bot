# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 52**

| Date | Headline |
|------|----------|
| 2026-08-20 | FalconX, Ethena bring USDe backing assets into $1B institutional credit facility… |
| 2026-08-20 | Bitcoin price hits 11-week high as US Treasury doubles debt buyback size… |
| 2026-08-20 | SEC regulatory proposal marks ‘important’ step forward from ‘inapt’ crypto rules… |
| 2026-08-20 | Bearish crypto bets lose record $2.7 billion as bitcoin surges toward $70,000… |
| 2026-08-20 | Live updates: Bitcoin hits $71,000, ETFs draw $700 million in biggest inflows in… |

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
*README auto-updated: 2026-08-20 13:00 UTC*
