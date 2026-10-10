# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 52**

| Date | Headline |
|------|----------|
| 2026-10-10 | US plans to seize $1B in crypto linked to Iran this week: Scott Bessent… |
| 2026-10-10 | UK sanctions three crypto exchanges tied to Russian illicit funds… |
| 2026-10-10 | XRP Ledger patched decade-old bug that could create billions of dollars in XRP f… |
| 2026-10-10 | Blockchain.com Seeks Approval for US Prediction Markets and Crypto Derivatives… |
| 2026-10-10 | Ledger Probes Potential Theft of $87M in User Funds Tied to Crypto Wallet Resell… |

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
*README auto-updated: 2026-10-10 13:00 UTC*
