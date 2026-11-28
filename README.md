# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 54**

| Date | Headline |
|------|----------|
| 2026-11-28 | Franklin Templeton makes room for HYPE in crypto index ETF… |
| 2026-11-28 | Fed Governor Waller warns of "zombie chains" as tokenization grows… |
| 2026-11-28 | CFTC approves Backpack to run derivatives exchange and clearinghouse… |
| 2026-11-28 | CFTC orders Kalshi to pause certain Trump speech contracts… |
| 2026-11-28 | Binance receives in-principle approval, plans Asia hub in Bhutan… |

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
*README auto-updated: 2026-11-28 13:00 UTC*
