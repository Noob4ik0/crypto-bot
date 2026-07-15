# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 37**

| Date | Headline |
|------|----------|
| 2026-07-15 | U.S. CFTC moves to stop Kalshi from canceling trades as ordered by Michigan cour… |
| 2026-07-15 | Ethereum devs huddled in the Arctic Circle to fix the network. Here’s what to kn… |
| 2026-07-15 | Crypto companies raised $600m in April despite despite market downturn, VCs say… |
| 2026-07-15 | Kalshi says CFTC, Michigan orders leave it in ‘impossible position’… |
| 2026-07-15 | Live markets: Bitcoin, ether ETFs draw inflows as majors rise as much as 5%… |

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
*README auto-updated: 2026-07-15 13:00 UTC*
