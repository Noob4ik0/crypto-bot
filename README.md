# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 47**

| Date | Headline |
|------|----------|
| 2026-11-17 | Hackers inject credit card, crypto-stealing malware into 178 major websites… |
| 2026-11-17 | Trezor customer data exposed in 3rd partner breach this year… |
| 2026-11-17 | Wells Fargo's reported BlackRock bitcoin ETF holdings double to $2.35 billion… |
| 2026-11-17 | Goldman Sachs reports $1.22B in Ether ETFs as ETHA share count jumps… |
| 2026-11-17 | Solana Foundation takes majority stake in crypto data provider CoinGecko… |

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
*README auto-updated: 2026-11-17 13:00 UTC*
