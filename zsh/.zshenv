#!/usr/bin/env zsh

#Config
export DOTFILES="$HOME/.dotfiles"
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$XDG_CONFIG_HOME/cache
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"
export ZPLUGINDIR="$ZDOTDIR/plugins"

#History
export HISTFILE="$ZDOTDIR/.zhistory"
export HISTSIZE=10000
export SAVEHIST=10000

#Fzf
FZF_COLORS="bg+:-1,\
fg:gray,\
fg+:white,\
hl:yellow,\
hl+:red,\
border:gray,\
spinner:blue,\
info:green,\
pointer:red,\
marker:green,\
prompt:yellow"

export FZF_DEFAULT_OPTS="--height 60% \
--border \
--layout reverse \
--color '$FZF_COLORS' \
--prompt '󰔰 ' \
--pointer 󰜴 \
--marker 󰨃"

#Bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"