# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 55**

| Date | Headline |
|------|----------|
| 2026-08-08 | Why trillion-dollar asset manager T. Rowe Price put memecoins in its crypto ETF… |
| 2026-08-08 | Brazil's central bank orders exchanges to delay large crypto transfers abroad… |
| 2026-08-08 | Trillions in institutional money to flow into bitcoin, says Bitwise's Matt Houga… |
| 2026-08-08 | US spot Bitcoin ETFs post best week since April with $1B inflows… |
| 2026-08-09 | Brazil targets crypto fraud with up to 24-hour transfer hold… |

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
*README auto-updated: 2026-08-09 13:00 UTC*
