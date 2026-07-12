# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 21**

| Date | Headline |
|------|----------|
| 2026-07-11 | Bonzo Lend loses $9M in oracle exploit on Hedera… |
| 2026-07-11 | Nano Banana 2 Lite vs. Nano Banana 2: When to Save Your Money and When to Upgrad… |
| 2026-07-11 | Crypto IPO market stalls as capital rotates to AI and macro uncertainty weighs… |
| 2026-07-11 | Lending protocol Bonzo loses 77% of value locked as $9 million oracle exploit ra… |
| 2026-07-12 | Bitcoin’s BIP 110 fork deadline nears with miner support at zero… |

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
*README auto-updated: 2026-07-12 13:00 UTC*
