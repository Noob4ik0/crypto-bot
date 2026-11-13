# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 49**

| Date | Headline |
|------|----------|
| 2026-11-13 | North Korea's Binance hack faces U.S. crackdown as DOJ targets $1.2 billion in s… |
| 2026-11-13 | Trump nominates Hester Peirce successor among SEC, CFTC picks… |
| 2026-11-13 | Bitcoin ETFs are now down over $1.5 billion in net outflows for the year… |
| 2026-11-13 | Bitcoin firm Nakamoto owes Kraken $165 million, more than its entire market valu… |
| 2026-11-13 | DOJ moves to seize $1.2B from Binance hack, disrupts FaceStealer scam… |

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
*README auto-updated: 2026-11-13 13:00 UTC*
