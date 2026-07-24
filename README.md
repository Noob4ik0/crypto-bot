# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 45**

| Date | Headline |
|------|----------|
| 2026-07-24 | Nasdaq-Listed Zhibao Wants a Bitcoin Treasury, Plans to Sell $220M in Stock for … |
| 2026-07-24 | BlackRock, Coinbase and Strategy Pledge $15M to Quantum-Proof Bitcoin… |
| 2026-07-24 | BitMEX hit with 623 BTC lawsuit on day it announces shutdown… |
| 2026-07-24 | Crypto 'Wrench Attacks' Cost Victims $124M in Six Months, Up 12x: CertiK… |
| 2026-07-24 | BitMEX faces proposed class-action suit for theft, insider trading as crypto exc… |

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
*README auto-updated: 2026-07-24 13:00 UTC*
