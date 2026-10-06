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
| 2026-10-06 | Strive Adds $169M Bitcoin in Its Biggest Buy in Four Months… |
| 2026-10-06 | Solana Debuts Institutional Settlement Standard With J.P. Morgan Input… |
| 2026-10-06 | U.S. scraps proposed $10,000 reporting rule for for crypto sent to private walle… |
| 2026-10-06 | Solana Foundation unveils a program to settle institutional trades in seconds. J… |
| 2026-10-06 | Hong Kong officials double down on end-2026 deadline for crypto licensing bill… |

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
*README auto-updated: 2026-10-06 13:00 UTC*
