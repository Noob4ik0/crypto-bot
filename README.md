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
| 2026-08-11 | Trump Media’s bitcoin holdings shrink as crypto losses hit $361 million… |
| 2026-08-11 | Strategy turns 1,690 BTC into $108.6M STRC buyback… |
| 2026-08-11 | Thailand’s 0% crypto tax. Bitcoin Red Team forced to use Chinese AI: Asia Expres… |
| 2026-08-11 | U.S. SEC sets meeting to propose Reg Crypto to support certain digital assets of… |
| 2026-08-11 | A $2 trillion asset class is getting a new blockchain rail… |

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
*README auto-updated: 2026-08-11 13:00 UTC*
