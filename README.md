# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 58**

| Date | Headline |
|------|----------|
| 2026-07-26 | World Foundation Raises $52.5M to Scale Sam Altman’s ‘Proof of Human’ ID… |
| 2026-07-26 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |
| 2026-07-26 | Strategy shares soar 50% in a month as Bitcoin tops $80,000 ahead of Q1 earnings… |
| 2026-07-26 | Crypto exchange BitMart to shut down after nine years, BMX token crashes 58%… |
| 2026-07-26 | Bitcoin tops $80,000 price as Clarity Act nears Senate floor with new Fed chair … |

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
*README auto-updated: 2026-07-26 13:00 UTC*
