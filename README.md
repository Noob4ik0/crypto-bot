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
| 2026-10-21 | Solana’s Alpenglow launches on mainnet, targets 99% faster finality… |
| 2026-10-21 | Standard Chartered signs definitive deal to acquire Zodia Custody… |
| 2026-10-21 | PancakeSwap TVL tops $380M as major fee overhaul heads to vote… |
| 2026-10-22 | Bitcoin ETFs bag another $528M, taking 3-day haul past $1B… |
| 2026-10-22 | Chinese Prosecutors Seek to Confiscate $5.1B in Bitcoin Seized by UK in Qian Cas… |

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
*README auto-updated: 2026-10-22 13:00 UTC*
