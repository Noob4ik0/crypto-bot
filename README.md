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
| 2026-09-21 | Strategy's Bitcoin Pile Nears June Record After $76M Purchase… |
| 2026-09-22 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |
| 2026-09-22 | Manhattan US Attorney leading probe into Binance’s Iran compliance: Bloomberg… |
| 2026-09-22 | Animoca puts Currenc merger on ice, delaying its Nasdaq debut… |
| 2026-09-22 | Spot bitcoin ETFs attracted nearly $1 billion on Monday, the 9th largest inflow … |

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
*README auto-updated: 2026-09-22 13:00 UTC*
