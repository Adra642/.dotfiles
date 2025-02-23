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

export FZF_CTRL_T_OPTS="
  --walker-skip .git,node_modules,target,.gradle,.idea,.vscode,.cache,.angular
  --preview 'bat -n --color=always {}'
  --preview-window 'border-bold'
  --bind 'ctrl-/:change-preview-window(hidden|)'"

export FZF_DEFAULT_OPTS="--height 60% \
--border bold \
--reverse \
--color '$FZF_COLORS' \
--no-scrollbar \
--prompt '󰔰 ' \
--pointer 󰨃 \
--marker "

#Bat 
export BAT_THEME="base16"

export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export MANROFFOPT="-c"

#Bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"