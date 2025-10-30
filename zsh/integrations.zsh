# Zellij
[[ -x "$(command -v zellij)" ]] && eval "$(zellij setup --generate-auto-start zsh)"

# Fzf
[[ -x "$(command -v fzf)" ]] && source <(fzf --zsh)

# Angular CLI autocompletion
[[ -x "$(command -v ng)" ]] && source <(ng completion script)

# Bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
[ -s "$BUN_INSTALL/_bun" ] && source "$BUN_INSTALL/_bun"

# Cargo
export CARGO_HOME="${CARGO_HOME:-$HOME/.cargo}"

# export PATH=$PATH:$HOME/sonar-scanner-6.2.1.4610-linux-x64/bin