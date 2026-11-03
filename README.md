# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 57**

| Date | Headline |
|------|----------|
| 2026-11-03 | North Korea denies role in $6.3B Binance hack, points finger at US… |
| 2026-11-03 | South Korea urges exchanges to boost cold storage after Binance hack… |
| 2026-11-03 | Crypto investigators flag suspected $106M theft, $786K Solana bot drain… |
| 2026-11-03 | Arbitrum’s council moved $30 million of Binance hack funds without the hacker’s … |
| 2026-11-03 | North Korea denies role in $6.4 billion Binance hack after FBI points to TraderT… |

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
*README auto-updated: 2026-11-03 13:00 UTC*
