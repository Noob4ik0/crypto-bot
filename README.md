# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 59**

| Date | Headline |
|------|----------|
| 2026-08-22 | Bitcoin Climbs Higher as $1.2 Billion in Shorts Liquidated… |
| 2026-08-23 | Morning Minute: CFTC Will Give Crypto Clarity If Congress Won’t… |
| 2026-08-23 | Most Americans Say Trump's Crypto Profits Cross the Line: Poll… |
| 2026-08-23 | Crypto industry reels as April sees highest number of hacks ever… |
| 2026-08-23 | Hegseth recasts Bitcoin as national security asset amid Russia, China expansion… |

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
*README auto-updated: 2026-08-23 13:00 UTC*
