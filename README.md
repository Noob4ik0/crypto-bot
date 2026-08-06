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
| 2026-08-06 | Crypto firm RedotPay says it will defend itself ‘vigorously’ against Binance law… |
| 2026-08-06 | OpenAI and Anthropic's Rogue Models Hacked Real Companies. The Law Has No Answer… |
| 2026-08-06 | Ethereum Proposal Would Burn Staking Rewards to Zero if Half of ETH Is Staked… |
| 2026-08-06 | Bitcoin steadies above $64,000 as traders watch $100 billion SpaceX unlock… |
| 2026-08-06 | Bitcoin ETFs pull in $244M, 3-day inflow streak tops $626M… |

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
*README auto-updated: 2026-08-06 13:00 UTC*
