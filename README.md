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
| 2026-10-28 | Wall Street backbone DTCC brings $30 trillion securities closer to blockchain wi… |
| 2026-10-28 | Fed leaves interest rates unchanged, as expected… |
| 2026-10-28 | AI Security Startup Upwind Raises $400M at $3.8B Valuation… |
| 2026-10-29 | Fed Stands Pat, Bitcoin Holds Steady—But a December Rate Hike Is in Play… |
| 2026-10-29 | Bitcoin drops to $80,000 on Fed dissent, Samsung, Alphabet earnings; AI tokens s… |

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
*README auto-updated: 2026-10-29 13:00 UTC*
