# 🎨 ADRA.Dots

> Personal dotfiles for a beautiful, efficient, and modern terminal experience

My personal repository of configuration files for terminal applications, featuring color scheme management, custom Zsh theme, and integration across multiple tools.

![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)
![Shell](https://img.shields.io/badge/shell-Zsh-green.svg)

---

## ✨ Features

- 🎨 **Dynamic Color Schemes** - Python-based color scheme selector for unified theming
- 🐚 **Custom Zsh Configuration** - Optimized shell with plugins, completions, and custom theme
- 🖥️ **Multiple Terminal Support** - Configurations for Alacritty, WezTerm, and Zellij
- 🔧 **Modular Design** - Clean, organized, and easy to customize
- 📦 **Plugin Management** - Automatic plugin installation and loading
- 🚀 **Performance Optimized** - Fast startup with lazy loading

---

## 📁 Structure

```
dotfiles/
├── alacritty/           # Alacritty terminal configuration
│   ├── alacritty.toml
│   └── current_scheme.toml
├── color_selector/      # Dynamic color scheme management
│   ├── schemes/         # Individual color scheme files
│   ├── color_scheme_selector.py
│   ├── alacritty_color.py
│   ├── wezterm_color.py
│   ├── zellij_color.py
│   ├── constants.py
│   └── logger.py
├── fastfetch/           # System information tool config
│   └── config.jsonc
├── nvim/                # Neovim configuration
│   └── init.vim
├── wallpaper/           # Wallpaper management
│   └── wallpaper_selector.sh
├── wezterm/             # WezTerm terminal configuration
│   ├── wezterm.lua
│   └── color.lua
├── zellij/              # Zellij multiplexer configuration
│   ├── config.kdl
│   ├── layouts/
│   └── themes/
└── zsh/                 # Zsh shell configuration
    ├── .zshenv          # Environment variables
    ├── .zshrc           # Main configuration
    ├── aliases.zsh      # Command aliases
    ├── completion.zsh   # Completion settings
    ├── exports.zsh      # Exported variables
    ├── integrations.zsh # External tool integrations
    ├── plugins.zsh      # Plugin management
    └── theme.zsh        # Custom prompt theme
```

---

## 🚀 Quick Start

### Prerequisites

- **Zsh** - Shell
- **Git** - Version control
- **Python 3** - For color scheme selector
- **TOML library** - `pip install toml`

### Optional Dependencies

- **Alacritty** - GPU-accelerated terminal
- **WezTerm** - GPU-accelerated terminal with Lua config
- **Zellij** - Terminal multiplexer
- **Eza** - Modern `ls` replacement
- **Bat** - Cat clone with syntax highlighting
- **Fzf** - Fuzzy finder
- **Fastfetch** - System information tool

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/adra642/.dotfiles.git
   ```

2. **Set up Zsh configuration**
   ```bash
   # Create XDG config directory
   mkdir -p ~/.config/zsh
   
   # Link Zsh files
   ln -sf ~/.dotfiles/zsh/.zshenv ~/.zshenv
   ln -sf ~/.dotfiles/zsh/.zshrc ~/.config/zsh/.zshrc
   ```

3. **Link other configurations**
   ```bash
   # Alacritty
   ln -sf ~/.dotfiles/alacritty ~/.config/alacritty
   
   # WezTerm
   ln -sf ~/.dotfiles/wezterm ~/.config/wezterm
   
   # Zellij
   ln -sf ~/.dotfiles/zellij ~/.config/zellij
   
   # Fastfetch
   ln -sf ~/.dotfiles/fastfetch ~/.config/fastfetch
   
   # Neovim
   ln -sf ~/.dotfiles/nvim ~/.config/nvim
   ```

4. **Set up color schemes**
   ```bash
   # Copy color schemes to config directory
   mkdir -p ~/.config/color_selector/schemes
   cp ~/.dotfiles/color_selector/schemes/*.toml ~/.config/color_selector/schemes/
   ```

5. **Reload your shell**
   ```bash
   exec zsh
   ```

---

## 🎨 Color Scheme Selector

The color scheme selector is a Python-based tool that applies consistent theming across all terminal applications.

### Usage

```bash
# Run the color selector
color

# Or directly
python ~/.config/color_selector/color_scheme_selector.py
```

### Adding Custom Schemes

Create a new `.toml` file in `~/.config/color_selector/schemes/`:

```toml
# my_scheme.toml
[colors.primary]
background = "#000000"
foreground = "#FFFFFF"

[colors.normal]
black = "#000000"
red = "#FF0000"
# ... etc
```

The scheme will be automatically detected on next run!

---

## 🐚 Zsh Configuration

### Plugins

- **zsh-autosuggestions** - Fish-like autosuggestions
- **zsh-syntax-highlighting** - Fish-like syntax highlighting
- **zsh-completions** - Additional completion definitions

### Aliases

```bash
# File listing (using eza)
ls    # eza --icons
ll    # eza --icons -l
lla   # eza --icons -la
lt    # eza --icons --tree

# Utilities
color     # Color scheme selector
wallpaper # Random wallpaper setter
fonts     # Rebuild font cache

# Directory navigation
d         # Show directory stack
1-9       # Jump to directory in stack
```

### Prompt Theme

The custom prompt includes:
- Username (red)
- Current directory (green, last 2 components)
- Git branch (yellow) with status indicators:
  - `+N` - Staged files (green)
  - `!N` - Modified files (yellow)
  - `?N` - Untracked files (red)
- Command status indicator (cyan/red)

---

## 🔧 Customization

### Changing the Default Shell

```bash
chsh -s $(which zsh)
```

### Modifying the Prompt

Edit `~/.dotfiles/zsh/theme.zsh` to customize:
- Colors
- Components (username, directory, git info)
- Status indicators

### Adding New Aliases

Add to `~/.dotfiles/zsh/aliases.zsh`:
```bash
alias myalias="my command"
```

---

## 📝 File Descriptions

### Zsh Files

| File | Purpose |
|------|---------|
| `.zshenv` | Environment variables (loaded first, for all shells) |
| `.zshrc` | Main configuration (interactive shells only) |
| `aliases.zsh` | Command aliases |
| `completion.zsh` | Completion system configuration |
| `exports.zsh` | Exported variables for interactive features |
| `integrations.zsh` | External tool integrations (fzf, zellij, bun) |
| `plugins.zsh` | Plugin management and loading |
| `theme.zsh` | Custom prompt theme with git integration |

---

## 🙏 Acknowledgments

- [Alacritty](https://github.com/alacritty/alacritty) - GPU-accelerated terminal emulator
- [WezTerm](https://github.com/wez/wezterm) - GPU-accelerated terminal with Lua config
- [Zellij](https://github.com/zellij-org/zellij) - Terminal multiplexer
- [Zsh](https://www.zsh.org/) - Powerful shell
- [Eza](https://github.com/eza-community/eza) - Modern ls replacement
- [Bat](https://github.com/sharkdp/bat) - Cat clone with wings
- [Fzf](https://github.com/junegunn/fzf) - Fuzzy finder

---

<div align="center">

[⬆ Back to Top](#-adradots)

</div>