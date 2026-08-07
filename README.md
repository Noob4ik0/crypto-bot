# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 58**

| Date | Headline |
|------|----------|
| 2026-08-07 | Senators Push CFTC to Ban Wildfire Bets on Prediction Markets… |
| 2026-08-07 | Crypto Wrench Attacks on Pace for Record Year as $30M Stolen in 2026: Chainalysi… |
| 2026-08-07 | Japan FSA asks crypto exchanges to impose withdrawal delays to fight scams… |
| 2026-08-07 | Bitcoin whales load up on $1.2 billion in BTC as ETFs attract $750 million… |
| 2026-08-07 | Coldcard fallout shows up onchain as 210,000 bitcoin leaves old wallets… |

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
*README auto-updated: 2026-08-07 13:00 UTC*
