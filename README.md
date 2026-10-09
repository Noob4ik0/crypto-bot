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
| 2026-10-09 | Securitize brings Apple, Nvidia and Tesla to Solana, with NYSE trading in the wo… |
| 2026-10-09 | US government moves $1B in seized Bitcoin after $770M transfers… |
| 2026-10-09 | Ether bets were wiped out at six times bitcoin’s rate in crypto’s $1 billion flu… |
| 2026-10-09 | New tech to power bitcoin lending is set to debut with $500 million in commitmen… |
| 2026-10-09 | Dark web drug market operator sentenced to 40 years, forfeits $101 million in bi… |

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
*README auto-updated: 2026-10-09 13:00 UTC*
