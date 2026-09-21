# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 51**

| Date | Headline |
|------|----------|
| 2026-09-20 | Crypto industry reels as April sees highest number of hacks ever… |
| 2026-09-20 | Hong Kong jails ex-banker over $1.6B false credit, cryptocurrency bribes: Report… |
| 2026-09-21 | Hana Bank taps Euroclear blockchain for $100M bond issuance: Report… |
| 2026-09-21 | ZetaChain holders approve plan to wind down L1, move ZETA to Solana… |
| 2026-09-21 | Live updates: Bitcoin hits $85,000 as short liquidations hit $300 million in an … |

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
*README auto-updated: 2026-09-21 13:00 UTC*
