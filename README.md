# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 52**

| Date | Headline |
|------|----------|
| 2026-08-15 | Fake LinkedIn Crypto Job Scams Have Cost $11.8M: Singapore… |
| 2026-08-15 | Clarity survives (barely), Strategy sells and the untold story of Mastercard's $… |
| 2026-08-15 | Why the world’s second-largest Bitcoin mining power is shutting down rigs in its… |
| 2026-08-15 | The $11.2 billion in 2026 funding that killed crypto’s permissionless era… |
| 2026-08-15 | Bitcoin to $1M by 2030 is ‘mathematically impossible’ says Markus Thielen… |

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
*README auto-updated: 2026-08-16 13:00 UTC*
