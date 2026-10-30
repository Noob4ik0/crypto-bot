# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 30**

| Date | Headline |
|------|----------|
| 2026-10-30 | Binance hack drained wallets backing customer assets, reserve data shows… |
| 2026-10-30 | Binance loses $5.7 billion in 'biggest crypto hack in history'… |
| 2026-10-30 | Binance hacker splits $1.4 billion of bitcoin into 19 wallets that no one can fr… |
| 2026-10-30 | Binance hack bites India's largest crypto exchange as it curbs futures trading… |
| 2026-10-30 | Live updates: Binance finds more breaches in $6.3 billion hack; AI spending fear… |

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
*README auto-updated: 2026-10-30 13:00 UTC*
