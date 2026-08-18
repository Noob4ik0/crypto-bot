# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 53**

| Date | Headline |
|------|----------|
| 2026-08-18 | Prediction Markets Give the Fed 74% Odds of Standing Pat in September… |
| 2026-08-18 | Treasury Proposes Rules Defining Who Can Legally Sell Stablecoins in US… |
| 2026-08-18 | Alleged $165M crypto Ponzi mastermind faces US charges after Fiji deportation… |
| 2026-08-18 | Wall Street Pushback Halts SEC's Crypto Fundraising Framework, Sources Say… |
| 2026-08-18 | XRP sinks below $1 for first time since 2024 even as Korean bank adopts Ripple P… |

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
*README auto-updated: 2026-08-18 13:00 UTC*
