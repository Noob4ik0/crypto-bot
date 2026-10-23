# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 45**

| Date | Headline |
|------|----------|
| 2026-10-22 | a16z Drops Crypto From Its Name, Widens Bets to AI and Frontier Tech… |
| 2026-10-23 | New DeepSeek ban in US, Swiss-Asia crypto ties deepen: Asia Express… |
| 2026-10-23 | Switzerland approves first spot Bitcoin ETF for retail investors… |
| 2026-10-23 | Bitcoin ETFs bleed $635M as October slides back into the red… |
| 2026-10-23 | India's largest exchange denies hack after sleuths pointed to $16 million in sus… |

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
*README auto-updated: 2026-10-23 13:00 UTC*
