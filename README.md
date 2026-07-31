# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 56**

| Date | Headline |
|------|----------|
| 2026-07-31 | Strategy books $8.2 billion Q2 loss on bitcoin price decline… |
| 2026-07-31 | Strategy posts $8.2B Q2 loss as Bitcoin slump drives unrealized losses… |
| 2026-07-31 | Coinbase Q2 profit misses estimates despite record crypto market share… |
| 2026-07-31 | Major bitcoin wallet flaw drains 594 BTC in 25-minute sweep… |
| 2026-07-31 | Bitcoin ETFs post $233M inflows, pushing week back into the green… |

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
*README auto-updated: 2026-07-31 13:00 UTC*
