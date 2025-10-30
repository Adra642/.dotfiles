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

+vi-git-count-files() {
    local untracked_count staged_count modified_count
    local git_status
    
    # Obtener el estado de git
    git_status=$(git status --porcelain 2>/dev/null) || return
    
    # Retornar temprano si no hay cambios
    [[ -z "$git_status" ]] && return
    
    # Contar en un solo paso usando awk (más eficiente)
    while IFS= read -r line; do
        case "${line:0:2}" in
            "??") ((untracked_count++)) ;;
            [MADRC]?) ((staged_count++)) ;;
            ?[MD]) ((modified_count++)) ;;
        esac
    done <<< "$git_status"
    
    # Limpiar misc antes de añadir para controlar el orden
    hook_com[misc]=''
    
    # Mostrar contadores con sus símbolos en el orden: staged, unstaged, untracked
    if [[ $staged_count -gt 0 ]]; then
        hook_com[misc]+=" %F{green}+${staged_count}%f"
    fi
    
    if [[ $modified_count -gt 0 ]]; then
        hook_com[misc]+=" %F{yellow}!${modified_count}%f"
    fi
    
    if [[ $untracked_count -gt 0 ]]; then
        hook_com[misc]+=" %F{red}?${untracked_count}%f"
    fi
    
    # Configurar como vacío para que no se use el unstaged por defecto
    hook_com[unstaged]=''
}

+vi-git-custom-action() {
    # Personalizar los nombres de las acciones
    case ${hook_com[action]} in
        merge)
            hook_com[action]=" merge"
            ;;
        rebase)
            hook_com[action]=" rebase"
            ;;
        cherry-pick)
            hook_com[action]=" pick"
            ;;
        *)
            ;;
    esac
}

zstyle ':vcs_info:git:*' check-for-changes true
zstyle ':vcs_info:git:*' formats ' %F{yellow}[%F{red} %b%F{yellow}]%m'
zstyle ':vcs_info:git:*' actionformats ' %F{yellow}[%F{red} %b%F{yellow}|%F{cyan}%a%F{yellow}]%m'
zstyle ':vcs_info:git*+set-message:*' hooks git-count-files git-custom-action
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