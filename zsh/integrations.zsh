#!/usr/bin/env zsh

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# External Tool Integrations
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Zellij - Terminal multiplexer
if [[ -z "$ZELLIJ" && -x "$(command -v zellij)" ]]; then
    exec zellij attach -c default
fi

# Fzf - Fuzzy finder
[[ -x "$(command -v fzf)" ]] && source <(fzf --zsh)

# Bun - JavaScript runtime (completions)
[[ -s "$BUN_INSTALL/_bun" ]] && source "$BUN_INSTALL/_bun"
