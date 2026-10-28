# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 28**

| Date | Headline |
|------|----------|
| 2026-10-27 | VanEck launches diversified ETF combining stocks, bonds and Bitcoin exposure… |
| 2026-10-28 | Ripple, Robinhood expand partnership to bring RLUSD to retail and institutional … |
| 2026-10-28 | Bitcoin nears $81,000 ahead of Fed decision as ZEC jumps 8%… |
| 2026-10-28 | Bithumb hacked through employee system as South Korean financial firms face cybe… |
| 2026-10-28 | Bitcoin ETF inflows climb to $176M as BTC rebounds above $80K… |

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
*README auto-updated: 2026-10-28 13:00 UTC*
