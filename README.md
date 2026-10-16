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
| 2026-10-16 | Binance.US seeks $1B valuation in potential $100M funding round: Report… |
| 2026-10-16 | White House crypto council chief Patrick Witt steps down… |
| 2026-10-16 | Russia Will Soon Ban Peer-to-Peer Bitcoin Trading, Central Bank Confirms… |
| 2026-10-16 | Mastercard and BVNK Launch 'Global Money Platform' to Merge Fiat and Stablecoins… |
| 2026-10-16 | Capital B reports $78M H1 loss driven by Bitcoin impairment charge… |

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
*README auto-updated: 2026-10-16 13:00 UTC*
