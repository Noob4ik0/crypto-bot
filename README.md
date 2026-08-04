# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 60**

| Date | Headline |
|------|----------|
| 2026-08-04 | Kenya moves 30 million academic credentials onto Avalanche blockchain… |
| 2026-08-04 | BlackRock launches tokenized money market funds for stablecoin reserves… |
| 2026-08-04 | Bitcoin nears $64,000 as traders look past the fourth Coldcard sweep… |
| 2026-08-04 | Nigeria sets crypto tax collection rules for digital asset platforms… |
| 2026-08-04 | BlackRock debuts tokenized access to $311 billion of money market funds in Europ… |

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
*README auto-updated: 2026-08-04 13:00 UTC*
