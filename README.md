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
| 2026-11-24 | BlackRock launches tokenized money market fund accepting stablecoins in Hong Kon… |
| 2026-11-25 | South Korea proposes bank-led stablecoins, 20% cap on crypto exchange stakes… |
| 2026-11-25 | Ansem Meme Coin Crashes After $2.57 Million Wallet Drain, Bullpen Confirms Secur… |
| 2026-11-25 | South Korea’s crypto bill could move stablecoin race beyond token issuance… |
| 2026-11-25 | Justice Department Moves to Forfeit $1.1B in USDC From North Korea's Binance Hac… |

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
*README auto-updated: 2026-11-25 13:00 UTC*
