# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 44**

| Date | Headline |
|------|----------|
| 2026-07-23 | Zilliqa Ledger app vulnerability lets attackers recover signer’s private keys… |
| 2026-07-23 | Hugging Face CEO Thanks Chinese AI for Saving the Day After OpenAI Hack… |
| 2026-07-23 | AFX protocol reportedly loses $24M in bridge exploit… |
| 2026-07-23 | Hackers steal $31.6M in 2 crypto bridge attacks within 7 hours… |
| 2026-07-23 | Bitcoin, Ethereum-linked protocols lose $35 million in multiple attacks hours ap… |

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
*README auto-updated: 2026-07-23 13:00 UTC*
