# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 61**

| Date | Headline |
|------|----------|
| 2026-11-06 | Live updates: Bitcoin drops more than 5% as stocks close out worst day since Apr… |
| 2026-11-06 | Fed, OCC check US banks after Binance hack as experts flag security risks… |
| 2026-11-06 | Zcash’s landmark NU7 upgrade goes live, speeding up private payments… |
| 2026-11-06 | Europe’s largest asset manager Amundi tokenizes equity index fund on Ethereum… |
| 2026-11-06 | Greece approves 10% tax on crypto gains and 15% levy on DeFi income… |

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
*README auto-updated: 2026-11-06 13:00 UTC*
