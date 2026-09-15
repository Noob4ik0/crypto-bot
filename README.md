# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 19**

| Date | Headline |
|------|----------|
| 2026-09-15 | Symbiosis says recovered 15 BTC from bridge hack, offers 20% bounty… |
| 2026-09-15 | Strategy Buys Back $139 Million of STRC, Bitcoin Stack Frozen for Second Week… |
| 2026-09-15 | U.S. DOJ seeks $61 million in what it calls Iran's crypto-laundered black market… |
| 2026-09-15 | Live updates: Bitcoin slides from nearly $80,000 as Senate votes on Clarity Act… |
| 2026-09-15 | Live updates: Bitcoin slides to $77,000 as Senate votes on Clarity Act… |

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
*README auto-updated: 2026-09-15 13:00 UTC*
