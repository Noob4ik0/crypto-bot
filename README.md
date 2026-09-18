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
| 2026-09-18 | Real stocks are finally coming on blockchain. Here’s how the SEC wants it to wor… |
| 2026-09-18 | OG.com cleared by SEC to offer single-stock futures, says Crypto.com CEO… |
| 2026-09-18 | Bank of Japan raises interest rates by 25 basis points. Bitcoin tops $77,000… |
| 2026-09-18 | Iran’s Strait of Hormuz toll booth ran through a bitcoin exchange, U.S. says… |
| 2026-09-18 | UAE, Sweden Arrest Seven Over $7.1M Crypto Laundering Ring Linked to Contract Ki… |

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
*README auto-updated: 2026-09-18 13:00 UTC*
