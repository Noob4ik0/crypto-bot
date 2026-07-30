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
| 2026-07-30 | Fed holds rates steady, extending pause as markets await Kevin Warsh's policy ro… |
| 2026-07-30 | Binance.US to attempt prediction markets entry as CFTC-licensed entity, says CEO… |
| 2026-07-30 | Japanese game developer launches Bitcoin, altcoin fund with SBI… |
| 2026-07-30 | Ethereum Price Stalls as Fed Rate Decision Looms… |
| 2026-07-30 | Bitcoin ETF inflows return as Ether funds slip into outflows… |

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
*README auto-updated: 2026-07-30 13:00 UTC*
