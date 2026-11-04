# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 59**

| Date | Headline |
|------|----------|
| 2026-11-04 | Binance net outflows reach $5.3 billion after record hack. CEO says recovery und… |
| 2026-11-04 | ZachXBT identifies French bank as alleged victim of $133M crypto theft… |
| 2026-11-04 | Jack Dorsey's Block faces $764 million DOJ settlement as bitcoin profit plunges … |
| 2026-11-04 | Democrats surge toward Senate, House majorities, with crypto braced for new dire… |
| 2026-11-04 | ZachXBT names French bank Crédit Mutuel Arkéa as suspected victim of $133 millio… |

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
*README auto-updated: 2026-11-04 13:00 UTC*
