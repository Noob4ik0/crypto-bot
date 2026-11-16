# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 46**

| Date | Headline |
|------|----------|
| 2026-11-14 | Bank of Russia clears 17 crypto exchangers as Sberbank and VTB ready retail trad… |
| 2026-11-14 | Drift to issue ‘recovery tokens’ in wake of $295m hack… |
| 2026-11-15 | RWA protocol stUSDT winds down three years after $2.3B TVL peak… |
| 2026-11-16 | Bitcoin miners were hijacked and their BTC rewards redirected to an attacker… |
| 2026-11-16 | FOMC minutes, Nvidia earnings, Russia’s retail crypto rules: Crypto Week Ahead… |

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
*README auto-updated: 2026-11-16 13:00 UTC*
