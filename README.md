# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 38**

| Date | Headline |
|------|----------|
| 2026-09-17 | US lawmakers advance bill to lock Trump’s Bitcoin reserve into law… |
| 2026-09-17 | Bitcoin absorbs Fed rate hike as officials see more tightening… |
| 2026-09-17 | Zcash jumps 23% as bitcoin and major tokens rise despite Fed’s first hike since … |
| 2026-09-17 | Ripple adds XRP payments to Stripe and Tempo’s AI standard in new developer kit… |
| 2026-09-17 | Live updates: Zcash jumps 17% as $345 million of liquidations hit crypto traders… |

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
*README auto-updated: 2026-09-17 13:00 UTC*
