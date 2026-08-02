# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 57**

| Date | Headline |
|------|----------|
| 2026-08-01 | Minnesota crypto ATM ban goes into effect after reported $1M losses… |
| 2026-08-02 | Bitcoin cold-wallet attack spreads to 4,500 addresses as losses near $89 million… |
| 2026-08-02 | Onchain, in court: What happened in crypto legal news this week… |
| 2026-08-02 | $38M in Bitcoin Drained by Coldcard Key Flaw Its Maker Thinks AI Found… |
| 2026-08-02 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |

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
*README auto-updated: 2026-08-02 13:00 UTC*
