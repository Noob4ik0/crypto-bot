# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 25**

| Date | Headline |
|------|----------|
| 2026-08-24 | Jackson  Hole Symposium, U.S. PCE prices, IREN earnings: Crypto Week Ahead… |
| 2026-08-24 | Strategy raises $2 billion through MSTR sales and creates new USD Cash pool… |
| 2026-08-25 | Grayscale Launches Zcash ETF Following Critical Privacy Flaw That Rocked the Cry… |
| 2026-08-26 | Crypto CEO Faces US Extradition Over Alleged $20 Million Token Scheme… |
| 2026-08-27 | Charles Schwab adda Solana, Avalanche and Chainlink to nascent crypto platform… |

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
*README auto-updated: 2026-08-28 13:00 UTC*
