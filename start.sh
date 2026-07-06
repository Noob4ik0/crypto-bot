#!/bin/bash
SESSION="cryptobot"
BOT_DIR="$(dirname "$0")"
tmux kill-session -t $SESSION 2>/dev/null
tmux new-session -d -s $SESSION -x 220 -y 50
tmux send-keys -t $SESSION "cd $BOT_DIR && source venv/bin/activate && python bot_v2.py" Enter
echo "CryptoBot v2 launched — tmux attach -t $SESSION"
