# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 58**

| Date | Headline |
|------|----------|
| 2026-08-08 | Treasury Sanctions Crypto Exchanges It Says Laundered Millions for Iran… |
| 2026-08-08 | Bitcoin Payment Service BTCPay Warns Critical Flaw Is Under Active Attack… |
| 2026-08-08 | New XRP Ledger amendments target $530 million in tokenized Wall Street assets… |
| 2026-08-08 | Bitcoin Wallet Dormant Since 2011 Moves Millions in BTC… |
| 2026-08-08 | U.S. Senate opens first stage of crypto Clarity Act voting to give bill a chance… |

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
*README auto-updated: 2026-08-08 13:00 UTC*
