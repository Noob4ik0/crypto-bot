# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 54**

| Date | Headline |
|------|----------|
| 2026-10-03 | Crypto’s billions are back, but the premiums aren’t… |
| 2026-10-03 | Once a $2.3 Billion Network, Ethereum Layer-2 Blast Is Shutting Down… |
| 2026-10-03 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |
| 2026-10-03 | Chainalysis Used AI to Trace the $387M Bitget Hack Back to North Korea… |
| 2026-10-04 | Aave secures emergency hearing to void ‘catastrophic’ restraining order… |

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
*README auto-updated: 2026-10-04 13:00 UTC*
