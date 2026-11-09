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
| 2026-11-07 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |
| 2026-11-07 | U.S. Treasury moves to cut off crypto exchange MEXC over $16 billion in alleged … |
| 2026-11-07 | Gnosis Pay breach exposes card numbers, home addresses and linked crypto wallets… |
| 2026-11-09 | Solana moves to scrap the transaction feature used in the $270 million Drift hac… |
| 2026-11-09 | Binance, Tether and Trump crypto firms face Senate records deadline… |

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
*README auto-updated: 2026-11-09 13:00 UTC*
