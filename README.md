# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 53**

| Date | Headline |
|------|----------|
| 2026-08-21 | Bearish crypto bets lose record $3 billion as bitcoin tops $71,000… |
| 2026-08-21 | CFTC chair says agency will move forward on crypto regulation if CLARITY fails… |
| 2026-08-21 | Bitcoin miners pour billions into AI as capex outpaces revenue 15-to-1… |
| 2026-08-21 | Live updates: Bitcoin, ether ETFs pull in $800 million as inflows surge for a se… |
| 2026-08-21 | Treasury's latest measure isn't QE or YCC. Still, bitcoin is skyrocketing. Here'… |

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
*README auto-updated: 2026-08-21 13:00 UTC*
