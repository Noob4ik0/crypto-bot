# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 16**

| Date | Headline |
|------|----------|
| 2026-07-10 | Anthropic AI Oversight Board Adds Ben Bernanke, Who Oversaw 2008 Financial Crisi… |
| 2026-07-10 | Bitcoin gets a green light from a reliable momentum gauge. Here are key levels t… |
| 2026-07-10 | Labour MPs Push to Make UK Crypto Donation Ban Permanent… |
| 2026-07-10 | Circle soars after securing U.S. trust bank approval in crypto expansion… |
| 2026-07-10 | Circle Stock Jumps as Stablecoin Issuer Wins Final Federal Banking Charter Appro… |

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
*README auto-updated: 2026-07-11 13:00 UTC*
