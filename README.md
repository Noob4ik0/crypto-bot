# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 6**

| Date | Headline |
|------|----------|
| 2026-08-28 | Live updates: Bitcoin slips as Warsh talks tough on inflation at Jackson Hole… |
| 2026-08-31 | Sberbank plans to add ether and USDT as collateral for crypto-backed loans: Repo… |
| 2026-08-31 | Tom Lee's Bitmine Buys $131M of ETH in Largest Ethereum Purchase Since June… |
| 2026-09-01 | SEC proposes broad update to decades-old transfer agent rules with blockchain no… |
| 2026-09-02 | XRP ETFs pull in $170 million over 11 days. Goldman tops institutional holders… |

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
*README auto-updated: 2026-09-02 13:00 UTC*
