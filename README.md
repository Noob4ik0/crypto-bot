# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 49**

| Date | Headline |
|------|----------|
| 2026-10-20 | Crypto’s 2026 shutdown wave claims 82 projects. What went wrong?… |
| 2026-10-21 | Wallet Linked to Drift Exploit Sends $61 Million in Ethereum to Tornado Cash… |
| 2026-10-21 | Mt. Gox Pushes Repayment Deadline to 2027 With $2.8B in Bitcoin Still to Distrib… |
| 2026-10-21 | Crypto industry reels as April sees highest number of hacks ever… |
| 2026-10-21 | Drift exploiter sends $109M in Ether to Tornado Cash in 2 days… |

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
*README auto-updated: 2026-10-21 13:00 UTC*
