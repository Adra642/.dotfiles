#!/usr/bin/env zsh

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# External Tool Integrations
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Zellij - Terminal multiplexer
[[ -x "$(command -v zellij)" ]] && eval "$(zellij setup --generate-auto-start zsh)"

# Fzf - Fuzzy finder
[[ -x "$(command -v fzf)" ]] && source <(fzf --zsh)

# Bun - JavaScript runtime (completions)
[[ -s "$BUN_INSTALL/_bun" ]] && source "$BUN_INSTALL/_bun"
