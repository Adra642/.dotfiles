username() {
   echo "%{$fg[red]%}%n:%{$reset_color%}"
}

# current directory, two levels deep
directory() {
   echo "%{$fg[green]%}%2~%{$reset_color%}"
}

status() {
   echo "%(?:%{$fg[cyan]%}%1{󰶻%}:%{$fg[red]%}%1{󰶻%})"
}

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[yellow]%}±[%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[yellow]%}]✗ %{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[yellow]%}] "

PROMPT='$(username) $(directory) $(git_prompt_info)$(status)  '
