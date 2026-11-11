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
| 2026-11-11 | Hot US inflation raises odds of half-point Fed hike in December… |
| 2026-11-11 | LNbits rushes emergency patch after reported Bitcoin wallet thefts… |
| 2026-11-11 | CFTC warns Kalshi of imminent charges over notification of contracts: Politico… |
| 2026-11-11 | Initia confirms second exploit in 3 weeks, $3.27M stolen in latest attack… |
| 2026-11-11 | Stock ETF buyers pounce on dip as Bitcoin funds bleed $1.6 billion… |

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
*README auto-updated: 2026-11-11 13:00 UTC*
