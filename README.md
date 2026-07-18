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
| 2026-07-17 | UK sentences 2 hackers tied to $115M crypto ransom scheme… |
| 2026-07-18 | Three Men Jailed for Posing as Police in $5.3M UK Crypto Fraud… |
| 2026-07-18 | Crypto.com Hits $20B Valuation After $400M Citadel Securities Investment… |
| 2026-07-18 | Morgan Stanley Launches Bitcoin, Ethereum, and Solana Trading on E*Trade… |
| 2026-07-18 | Crypto industry reels as April sees highest number of hacks ever… |

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
*README auto-updated: 2026-07-18 13:00 UTC*
