#!/usr/bin/env zsh

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Plugin Management
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Clone a plugin, identify its init file, source it, and add it to fpath
function plugin-load {
    local repo plugdir initfile initfiles=()
    
    for repo in $@; do
        plugdir=$ZPLUGINDIR/${repo:t}
        initfile=$plugdir/${repo:t}.plugin.zsh
        
        # Clone plugin if not already present
        if [[ ! -d $plugdir ]]; then
            echo "Cloning $repo..."
            git clone -q --depth 1 --recursive --shallow-submodules \
                https://github.com/$repo $plugdir || {
                echo >&2 "Failed to clone '$repo'."
                continue
            }
        fi
        
        # Find and symlink init file if needed
        if [[ ! -e $initfile ]]; then
            initfiles=($plugdir/*.{plugin.zsh,zsh-theme,zsh,sh}(N))
            (( $#initfiles )) || { 
                echo >&2 "No init file found '$repo'."; 
                continue 
            }
            ln -sf $initfiles[1] $initfile
        fi
        
        # Add to fpath and source
        fpath+=$plugdir
        [[ -r $initfile ]] && . "$initfile"
    done
}

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Plugin List
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

plugins=(
    zsh-users/zsh-autosuggestions    # Fish-like autosuggestions
    zsh-users/zsh-syntax-highlighting # Fish-like syntax highlighting
    zsh-users/zsh-completions         # Additional completion definitions
)

plugin-load $plugins