# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 54**

| Date | Headline |
|------|----------|
| 2026-09-27 | Bitcoin's Quantum Problem: Three Ways Researchers Are Trying to Fix It… |
| 2026-09-28 | Zano rolls blockchain back a month after Gateway Address exploit… |
| 2026-09-28 | Bitcoin, Nasdaq futures decline as Trump won’t rule out more Iran strikes… |
| 2026-09-28 | Solana ETFs draw record $188 million in a week as Bitwise takes two-thirds of in… |
| 2026-09-28 | Bitget hacker moves $83 million in stolen XRP beyond reach of freeze controls… |

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
*README auto-updated: 2026-09-28 13:00 UTC*
