# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 61**

| Date | Headline |
|------|----------|
| 2026-11-07 | Binance hack is ‘cyber war,’ TRM Labs executive says… |
| 2026-11-07 | Binance hackers had 8-week intrusion window before $6.3B exploit: SEAL… |
| 2026-11-07 | Treasury Cuts Crypto Exchange MEXC Off From US Financial System… |
| 2026-11-07 | US Sanctions 45 More Targets Tied to Alleged Crypto Scam Empire Prince Group… |
| 2026-11-07 | $3.1B in Stolen Binance Crypto Has Yet to Be Laundered: Elliptic… |

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
*README auto-updated: 2026-11-07 13:00 UTC*
