# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 45**

| Date | Headline |
|------|----------|
| 2026-07-20 | Nigerian president signs order on approach to crypto regulation, taxes… |
| 2026-07-21 | Russia's First Comprehensive Crypto Law Is Two Votes Away From Passing… |
| 2026-07-21 | Cardano Triggers Hard Fork With First Community-Voted Upgrade… |
| 2026-07-21 | Grayscale files S-1 for first US Worldcoin ETF… |
| 2026-07-21 | UK Lawmakers Launch Inquiry Into Crypto Banking Access… |

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
*README auto-updated: 2026-07-21 13:00 UTC*
