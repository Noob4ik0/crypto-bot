# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 47**

| Date | Headline |
|------|----------|
| 2026-11-01 | Binance $6.3B record hack sparks pre-election political clashes… |
| 2026-11-01 | FBI confirms North Korea's role in $6 billion Binance hack, asks DeFi community … |
| 2026-11-01 | Recap: How Binance’s record $6.3B hack unfolded… |
| 2026-11-01 | As it happened: Binance’s record $6.3B crypto hack… |
| 2026-11-01 | Binance says phase one of withdrawals opens after $6.3B hack… |

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
*README auto-updated: 2026-11-01 13:00 UTC*
