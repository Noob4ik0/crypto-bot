# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 48**

| Date | Headline |
|------|----------|
| 2026-10-16 | Capital B reports $78M H1 loss driven by Bitcoin impairment charge… |
| 2026-10-16 | Morning Minute: Google Clears a Major Quantum Hurdle, Bitcoin Still Safe… |
| 2026-10-16 | Deutsche Bank prepares German crypto custody launch, eyes Asia: Report… |
| 2026-10-16 | Live updates: Crypto gives up more ground as AI selloff picks up steam… |
| 2026-10-17 | Satoshi-era bitcoin faces a bigger quantum threat after Google’s new Willow brea… |

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
*README auto-updated: 2026-10-17 13:00 UTC*
