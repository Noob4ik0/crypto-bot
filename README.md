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
| 2026-08-23 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |
| 2026-08-24 | Bitcoin tops $80,000 price as Clarity Act nears Senate floor with new Fed chair … |
| 2026-08-24 | Term Finance loses estimated $8.5M in vault governance exploit… |
| 2026-08-24 | Crypto holds big weekly rally as Warsh’s Jackson Hole debut comes into focus… |
| 2026-08-24 | Jackson  Hole Symposium, U.S. PCE prices, IREN earnings: Crypto Week Ahead… |

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
*README auto-updated: 2026-08-24 13:00 UTC*
