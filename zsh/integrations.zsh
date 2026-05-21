#!/usr/bin/env zsh

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# External Tool Integrations
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Zellij - Terminal multiplexer
# if [[ -z "$ZELLIJ" && -x "$(command -v zellij)" ]]; then
#    exec zellij attach -c default
# fi

# Fzf - Fuzzy finder
[[ -x "$(command -v fzf)" ]] && source <(fzf --zsh)

if [[ -z "$TMUX" ]] && [[ $- == *i* ]] && command -v tmux &> /dev/null; then
    tmux attach-session -t main || tmux new-session -s main
fi