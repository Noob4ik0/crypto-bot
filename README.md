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
| 2026-10-14 | Strive raising $500 million to buy additional bitcoin with new preferred share c… |
| 2026-10-14 | Largest Philippines crypto exchange, Coins.ph, said to face central bank regulat… |
| 2026-10-14 | Russia clears Sberbank for crypto trading ahead of December launch… |
| 2026-10-14 | Ripple adds Stripe-owned wallets to XRP Ledger as AI payments pass 14 million… |
| 2026-10-14 | Standard Chartered unlocks direct bitcoin and ether trading for affluent UAE cli… |

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
*README auto-updated: 2026-10-14 13:00 UTC*
