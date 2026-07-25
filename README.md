# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 48**

| Date | Headline |
|------|----------|
| 2026-07-25 | Poolin was bitcoin's biggest mining pool and now it's filing for bankruptcy… |
| 2026-07-25 | Bitcoin treasury companies sell up, repay debt, pivot to AI as share prices coll… |
| 2026-07-25 | World Foundation raises $52.5M in Pantera-led funding to expand World ID infrast… |
| 2026-07-25 | Bitcoin falls under $64K as surging US bond yields boost Fed rate-hike odds… |
| 2026-07-25 | Ethereum ETFs close week in red, end 5-day inflow streak… |

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
*README auto-updated: 2026-07-25 13:00 UTC*
