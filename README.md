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
| 2026-11-26 | Nvidia agrees to $290M settlement over crypto mining revenue disclosures… |
| 2026-11-26 | Bitcoin ETFs near $5B in record monthly outflows amid AI stock rout… |
| 2026-11-26 | Bill to lock up U.S. government bitcoin for 20 years advances to full House… |
| 2026-11-26 | $7 billion of bitcoin options expire Friday, and the biggest bets look starkly d… |
| 2026-11-26 | Bitcoin ETF November outflows top $5B, Morgan Stanley bucks trend… |

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
*README auto-updated: 2026-11-26 13:00 UTC*
