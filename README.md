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
| 2026-11-10 | Avalanche’s AVAX leads crypto gains following NYSE tokenization deal… |
| 2026-11-10 | Analysts see no broader ‘contagion’ from $6.3B Binance hack… |
| 2026-11-10 | Bitcoin miner MARA sold 13,597 BTC for $1.1 billion in six weeks, plans to sell … |
| 2026-11-10 | The $2.85B Binance hackers lost shows why the UK needs stablecoin freeze rules… |
| 2026-11-10 | Live news: Traders price in fed rate hike for December as bitcoin and gold retre… |

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
*README auto-updated: 2026-11-10 13:00 UTC*
