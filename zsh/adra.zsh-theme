autoload -Uz vcs_info

username() {
   echo "%B%F{red}%n:%f%b"
}

directory() {
   echo "%F{green}%2~%f"
}

status() {
   echo " $(if [[ $? -eq 0 ]]; then echo "%F{cyan}"; else echo "%F{red}"; fi)󰶻%f"
}

zstyle ':vcs_info:git:*' check-for-changes true
zstyle ':vcs_info:git:*' unstagedstr '✗'
zstyle ':vcs_info:git:*' formats ' %F{yellow}±[%F{red}%b%F{yellow}]%u'
zstyle ':vcs_info:git:*' actionformats ' %F{yellow}±[%F{red}%b%F{yellow}|%F{cyan}%a%F{yellow}]%u%c'
zstyle ':vcs_info:*' enable git

precmd() {
   vcs_info
}

git_branch() {
   if [[ -n ${vcs_info_msg_0_} ]]; then
      echo "${vcs_info_msg_0_}"
   fi
}

adra() { 
   setopt PROMPT_SUBST
   PROMPT='$(username) $(directory)$(git_branch)$(status) '
}

adra