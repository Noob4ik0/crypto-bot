# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 54**

| Date | Headline |
|------|----------|
| 2026-08-22 | Laser Digital gets Japan’s first crypto exchange approval in 4 years… |
| 2026-08-22 | Bitcoin ETFs draw $608M as Ether ETFs see largest inflow since October… |
| 2026-08-22 | Coldcard Adds New Security Measures After $130 Million Bitcoin Exploit… |
| 2026-08-22 | How a Treasury buyback tweak helped bitcoin surge 25% to nearly $80,000 in days… |
| 2026-08-22 | Wall Street and Washington Fuel Bitcoin Rally: Here's What's Going On… |

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
*README auto-updated: 2026-08-22 13:00 UTC*
