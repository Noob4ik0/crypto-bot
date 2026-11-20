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
| 2026-11-20 | Hackers Leak Visa, Mastercard and JPMorgan Customer Data… |
| 2026-11-20 | Institutions pile back into US Bitcoin ETFs in Q3 after selling streak… |
| 2026-11-20 | Here's what's crashing gold and likely weighing on bitcoin too… |
| 2026-11-20 | Big money bought a net $4 billion of bitcoin funds in Q3, ending 9 months of sel… |
| 2026-11-20 | Ethereum’s next big upgrade is pushed into 2027 by apps it would break… |

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
*README auto-updated: 2026-11-20 13:00 UTC*
