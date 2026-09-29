# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 55**

| Date | Headline |
|------|----------|
| 2026-09-29 | US SEC follows CFTC in staff guidance for crypto… |
| 2026-09-29 | NEAR Intents says it blocked $50M tied to Bitget hackers… |
| 2026-09-29 | Coinbase gets CFTC approval for US derivatives clearinghouse… |
| 2026-09-29 | Near Intents blocks $50 million in Bitget hacker swaps, here's what happened… |
| 2026-09-29 | Blockchain.com targets $500 million IPO this year at up to $6 billion valuation… |

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
*README auto-updated: 2026-09-29 13:00 UTC*
