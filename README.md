# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 41**

| Date | Headline |
|------|----------|
| 2026-10-23 | China targets 2030 for its national blockchain network buildout… |
| 2026-10-23 | Crypto Scammers Who Used Prayer Groups to Lure Victims Must Pay $1.3 Billion, Sa… |
| 2026-10-23 | Initia halts blockchain after exploit reportedly drains over $2.6M… |
| 2026-10-23 | US senator probes Tether after reported deal with ex-Trump crypto adviser… |
| 2026-10-24 | Senate Democrat Probes Tether Payments to Ex-White House Crypto Adviser’s Firm… |

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
*README auto-updated: 2026-10-25 13:00 UTC*
