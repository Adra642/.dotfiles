#!/usr/bin/env zsh

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Directories
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

export ZPLUGINDIR="${ZPLUGINDIR:-$ZDOTDIR/plugins}"

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# History Configuration
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

export HISTFILE="$ZDOTDIR/.zhistory"
export HISTSIZE=10000
export SAVEHIST=10000

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Fzf Configuration
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
--walker file,hidden,dir \
--border bold \
--reverse \
--color '$FZF_COLORS' \
--no-scrollbar \
--prompt '󰔰 ' \
--pointer 󰨃 \
--marker "

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Bat Configuration
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

export BAT_THEME="base16"

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Man Pages
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export MANROFFOPT="-c"