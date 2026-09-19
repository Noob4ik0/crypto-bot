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
| 2026-09-19 | CFTC Kicks Off Crypto Rulemaking, Bypassing a Stalled Congress… |
| 2026-09-19 | Treasury Sanctions Crypto Exchange Behind Iran's Bitcoin Tolls on Hormuz Ships… |
| 2026-09-19 | CFTC Opens Door for Crypto Apps to Offer Regulated Derivatives Access… |
| 2026-09-19 | Aave secures emergency hearing to void ‘catastrophic’ restraining order… |
| 2026-09-19 | Hong Kong jails former banker over $1.6B false credit, cryptocurrency bribes: Re… |

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
*README auto-updated: 2026-09-19 13:00 UTC*
