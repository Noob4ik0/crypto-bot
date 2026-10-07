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
| 2026-10-07 | Another Zcash ETF Is Coming: Winklevoss Twins File for 'WINK'… |
| 2026-10-07 | Circle, Ripple and Standard Chartered Back OKX at Flat $25B Valuation… |
| 2026-10-07 | Morning Minute: The CFTC Reveals Plan to Regulate Crypto Exchanges… |
| 2026-10-07 | U.S. government moves over $100 million in BTC and BNB. A sale hasn't been confi… |
| 2026-10-07 | Crypto liquidations hit $550M as Bitcoin price dips below $84K… |

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
*README auto-updated: 2026-10-07 13:00 UTC*
