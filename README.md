# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 51**

| Date | Headline |
|------|----------|
| 2026-09-23 | Binance takes $100M stake in Circle under expanded USDC deal… |
| 2026-09-23 | Crypto market cap reclaims $3 trillion as Bitcoin, altcoins rally… |
| 2026-09-23 | Solana starts testing upgrade that could cut finality from 12.8 seconds to 150 m… |
| 2026-09-23 | Bitcoin ETFs take in $1.7B in 2 days as BTC tops holder cost basis… |
| 2026-09-23 | Malicious iOS app FomoPeek linked to $580K crypto theft, SlowMist says… |

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
*README auto-updated: 2026-09-23 13:00 UTC*
