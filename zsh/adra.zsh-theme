username() {
   echo "%B%F{red}%n:%f%b"
}

directory() {
   echo "%F{green}%2~%f"
}

status() {
   echo "$(if [[ $? -eq 0 ]]; then echo "%F{cyan}"; else echo "%F{red}"; fi)󰶻%f"
}

adra() {
   # ZSH_THEME_GIT_PROMPT_PREFIX="%F{yellow}%f±[%F{red}%f"
   # ZSH_THEME_GIT_PROMPT_SUFFIX="%F{red}%"
   # ZSH_THEME_GIT_PROMPT_DIRTY="%F{yellow}%f]✗ %F{red}%"
   # ZSH_THEME_GIT_PROMPT_CLEAN="%%F{yellow}%f] "
   # $(git_prompt_info)
   
   PROMPT="$(username) $(directory) $(status) "
}

adra

