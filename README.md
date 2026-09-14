# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 9**

| Date | Headline |
|------|----------|
| 2026-09-13 | UniCredit seeks infrastructure partner for crypto trading, custody: Report… |
| 2026-09-14 | Crypto Billionaires Hand Reform UK $97M in Record Donations… |
| 2026-09-14 | Bitcoin Rises as Markets Digest Inflation Data Ahead of Fed Rate Decision… |
| 2026-09-14 | Blockstream Refuses Ransom for Return of $47M in Bitcoin from Liquid Hack: 'It I… |
| 2026-09-14 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |

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
*README auto-updated: 2026-09-14 13:00 UTC*
