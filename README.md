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
| 2026-09-23 | Crypto Exchange That Invented 100x Leverage Is No More: Here’s What BitMEX Users… |
| 2026-09-24 | Ex-SEC acting chair: Agency dropped crypto cases to avoid issues with credibilit… |
| 2026-09-24 | An AI Agent Just Hacked a Government Website for the First Time, Australia PM Sa… |
| 2026-09-24 | NYSE Taps Blockchain.com to Reach Crypto Investors With Tokenized Stocks… |
| 2026-09-24 | EU financial watchdogs warn quantum computing poses imminent threat to blockchai… |

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
*README auto-updated: 2026-09-24 13:00 UTC*
