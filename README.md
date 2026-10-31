# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 39**

| Date | Headline |
|------|----------|
| 2026-10-31 | Crypto liquidations jump to $1.57 billion as Binance hack sends bitcoin, ether l… |
| 2026-10-31 | Binance hackers raced to move billions before it could be frozen… |
| 2026-10-31 | Bitcoin stolen from Binance tops Tesla’s holdings and is over twice El Salvador’… |
| 2026-10-31 | Coinbase leads crypto stock selloff following $6.3B Binance hack… |
| 2026-10-31 | Binance $6.3B record hack sparks pre-election political chatter… |

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
*README auto-updated: 2026-10-31 13:00 UTC*
