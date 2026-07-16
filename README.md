# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 40**

| Date | Headline |
|------|----------|
| 2026-07-16 | President Trump expected to meet with senators to work on ethics concerns in cry… |
| 2026-07-16 | Revolut receives in-principle approval from UAE authorities for crypto services… |
| 2026-07-16 | US Senator blasts AG pick for ‘dismantling’ crypto unit, Trump’s CZ pardon… |
| 2026-07-16 | A bitcoin wallet dormant since the 2017 peak just moved $383 million… |
| 2026-07-16 | Ether outruns bitcoin as ETF money returns, almost all of from BlackRock's fund… |

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
*README auto-updated: 2026-07-16 13:00 UTC*
