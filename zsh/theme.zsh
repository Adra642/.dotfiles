#!/usr/bin/env zsh

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Prompt Theme Configuration
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

autoload -Uz vcs_info

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Prompt Components
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

username() {
    echo "%B%F{red}%n:%f%b"
}

directory() {
    echo "%F{green}%2~%f"
}

status() {
    echo " $(if [[ $? -eq 0 ]]; then echo "%F{cyan}"; else echo "%F{red}"; fi)󰶻%f"
}

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Git Status Integration
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

+vi-git-count-files() {
    local untracked_count staged_count modified_count
    local git_status
    
    # Check if we're in a git repository first
    git rev-parse --is-inside-work-tree &>/dev/null || return
    
    # Get git status
    git_status=$(git status --porcelain 2>/dev/null) || return
    
    # Return early if no changes
    [[ -z "$git_status" ]] && return
    
    # Count changes in a single pass (more efficient)
    while IFS= read -r line; do
        case "${line:0:2}" in
            "??") ((untracked_count++)) ;;
            [MADRC]?) ((staged_count++)) ;;
            ?[MD]) ((modified_count++)) ;;
        esac
    done <<< "$git_status"
    
    # Clear misc before adding to control order
    hook_com[misc]=''
    
    # Show counters with symbols in order: staged, modified, untracked
    if [[ $staged_count -gt 0 ]]; then
        hook_com[misc]+=" %F{green}+${staged_count}%f"
    fi
    
    if [[ $modified_count -gt 0 ]]; then
        hook_com[misc]+=" %F{yellow}!${modified_count}%f"
    fi
    
    if [[ $untracked_count -gt 0 ]]; then
        hook_com[misc]+=" %F{red}?${untracked_count}%f"
    fi
    
    # Set as empty so default unstaged is not used
    hook_com[unstaged]=''
}

+vi-git-custom-action() {
    # Customize action names
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

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VCS Info Configuration
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Prompt Setup
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

adra() {
    setopt PROMPT_SUBST
    PROMPT='$(username) $(directory)$(git_branch)$(status) '
}

adra