# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 29**

| Date | Headline |
|------|----------|
| 2026-10-26 | Aviva Investors launches tokenized share class of $29B Sterling fund on XRP Ledg… |
| 2026-10-26 | Bitcoin Wallet Fixes Critical Flaw That Redirected Funds to Attackers… |
| 2026-10-26 | NBA names Kalshi, Polymarket preferred exchanges, signs CFTC deal… |
| 2026-10-27 | Ripple wins final US approval for national trust bank… |
| 2026-10-27 | Ripple gets a final go-ahead to launch its own U.S. national trust bank… |

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
*README auto-updated: 2026-10-27 13:00 UTC*
