# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 59**

| Date | Headline |
|------|----------|
| 2026-08-05 | US yen intervention puts Bitcoin, risk assets on notice for liquidity flux… |
| 2026-08-05 | BlackRock Tokenizes $311B of European Money Market Funds With JP Morgan's Kinexy… |
| 2026-08-05 | Five Convicted of Imprisoning Crypto Millionaires in London 'Torture' Ordeal… |
| 2026-08-05 | New Ethereum proposal would cut issuance to zero if staked ETH reaches $112 bill… |
| 2026-08-05 | Boerse Stuttgart Digital, Tradias close European crypto merger… |

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
*README auto-updated: 2026-08-05 13:00 UTC*
