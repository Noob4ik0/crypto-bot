# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 29**

| Date | Headline |
|------|----------|
| 2026-07-14 | Morning Minute: BTC and ETH ETFs Flip Green After Lengthy Outflow Stretch… |
| 2026-07-14 | DePIN and crypto gaming led a surprising end-of-year rebound… |
| 2026-07-14 | Bitcoin slips as traders lift July Fed rate hike bets ahead of Inflation report… |
| 2026-07-14 | Bitcoin threatens $62K in risk-asset rout as President Trump says US will 'run' … |
| 2026-07-14 | US spot Bitcoin ETFs post $425M outflow after brief rebound… |

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
*README auto-updated: 2026-07-14 13:00 UTC*
