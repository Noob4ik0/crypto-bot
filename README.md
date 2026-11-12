# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 49**

| Date | Headline |
|------|----------|
| 2026-11-12 | OKX-ICE Tokenized Stock Venue Sets Launch, Turning to Crypto Companies After Big… |
| 2026-11-12 | Avalanche Won Over the NYSE. Now It Has to ‘Capture Value’ for AVAX… |
| 2026-11-12 | Binance CSO unwittingly foreshadowed $6.3B hack tactic months before attack… |
| 2026-11-12 | MSCI is dropping Strategy from its index, and the exclusion could hit its bitcoi… |
| 2026-11-12 | India’s financial crimes watchdog raids crypto exchanges CoinDCX and Delta over … |

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
*README auto-updated: 2026-11-12 13:00 UTC*
