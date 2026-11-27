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
| 2026-11-27 | ‘Very racist’ Netflix SBF series, BitMart’s $319M shortfall: Asia Express… |
| 2026-11-27 | BNB Chain details new layer-1 for trading, private finance and AI… |
| 2026-11-27 | Binance completes withdrawal recovery four weeks after $6.3B hack… |
| 2026-11-27 | Crypto on notice as hawkish Fed risks December ‘meltdown’… |
| 2026-11-27 | ESMA to overhaul EU’s MiCA crypto register in 2027… |

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
*README auto-updated: 2026-11-27 13:00 UTC*
