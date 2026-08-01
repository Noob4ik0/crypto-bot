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
| 2026-08-01 | US Treasury yields rise as TIPS challenge the inflation narrative… |
| 2026-08-01 | US Treasury Sanctions Iranian Firms Taking Bitcoin for Hormuz Passage… |
| 2026-08-01 | Crypto Kiosk Scams Cost Texans $57M as Lawmakers Weigh a Ban… |
| 2026-08-01 | How bitcoin cold wallets lost $70 million in an attack that never touched the de… |
| 2026-08-01 | Coldcard Bitcoin loss estimate rises to $70M after Galaxy analysis… |

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
*README auto-updated: 2026-08-01 13:00 UTC*
