# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 56**

| Date | Headline |
|------|----------|
| 2026-10-03 | Bank group sues U.S. regulator over granting crypto trust charters… |
| 2026-10-03 | Crypto traders are in risk-on mode as bitcoin dominance nears return to 60%… |
| 2026-10-03 | $4.2B crypto bank Anchorage Digital cuts 17% of workforce: Report… |
| 2026-10-03 | Crypto’s billions are back, but the premiums aren’t… |
| 2026-10-03 | Once a $2.3 Billion Network, Ethereum Layer-2 Blast Is Shutting Down… |

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
*README auto-updated: 2026-10-03 13:00 UTC*
