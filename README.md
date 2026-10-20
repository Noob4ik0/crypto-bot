# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 50**

| Date | Headline |
|------|----------|
| 2026-10-20 | Strive buys $335M in Bitcoin, boosting holdings to 36,818 BTC… |
| 2026-10-20 | Strategy buys $22M in Bitcoin, repurchases $193M in STRC… |
| 2026-10-20 | Strive Buys $335 Million in Bitcoin After Investors Pour In $369 Million… |
| 2026-10-20 | US Bitcoin ETFs draw $527M in biggest showing since September… |
| 2026-10-20 | Bitcoin ETFs just saw their biggest day in a month thanks entirely to BlackRock… |

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
*README auto-updated: 2026-10-20 13:00 UTC*
