# CryptoBot v2

Crypto news monitor that automatically posts important news to Farcaster.

AI scores each headline 1–10. Only scores ≥ 7 get published.

## How it works

1. Checks 7 RSS feeds every 30 minutes (CoinDesk, CoinTelegraph, Decrypt, TheBlock, Blockworks, Messari, DLNews)
2. Filters by crypto keywords
3. AI rates importance 1–10 via OpenRouter
4. Posts to Farcaster with relevant hashtags if score ≥ 7

## 📊 Activity (last 7 days)

**Posts published: 57**

| Date | Headline |
|------|----------|
| 2026-10-02 | The 'Largest Pure-Play' XRP Treasury Is About to Go Public… |
| 2026-10-02 | SEC moves to clear custody hurdle for advisers offering crypto… |
| 2026-10-02 | Near Intents Hacked for $3.8M Days After Denying North Korea-Linked Bitget Hacke… |
| 2026-10-02 | Zano exploiter minted more than a quadrillion fUSD before blockchain rollback… |
| 2026-10-02 | NEAR Intents says it’s identified the hacker, gives 48-hour ultimatum… |

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
*README auto-updated: 2026-10-02 13:00 UTC*
