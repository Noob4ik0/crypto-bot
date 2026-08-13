# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 53**

| Date | Headline |
|------|----------|
| 2026-08-13 | Hawaii crypto ATM ban to take effect on Oct. 1… |
| 2026-08-13 | Bitcoin eyes $63K as US CPI relief sends September Fed rate pause odds to 60%… |
| 2026-08-13 | Solana neared a freeze threshold Wednesday, Marinade Finance says. The Foundatio… |
| 2026-08-13 | Metaplanet denies selling bitcoin worth $320 million… |
| 2026-08-13 | Live Markets: U.S. inflation is stickier than July’s mild CPI reading suggests… |

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
*README auto-updated: 2026-08-13 13:00 UTC*
