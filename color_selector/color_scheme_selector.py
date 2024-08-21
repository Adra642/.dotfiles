import os
import toml
from pathlib import Path
import shutil
import subprocess

from zellij_color import set_zellij_color_scheme
from wezterm_color import set_wezterm_color_scheme
from alacritty_color import set_alacritty_color_scheme

CONFIG_DIR = Path(os.environ['HOME']) / '.config'
COLOR_SCHEMES_FILE = CONFIG_DIR / 'color_selector' / 'color_schemes.toml'
ALACRITTY_THEME_FILE = CONFIG_DIR / 'alacritty' / 'current_scheme.toml'
ZELLIJ_THEME_FILE = CONFIG_DIR / 'zellij' / 'theme' / 'scheme.kdl'
WEZTERM_THEME_FILE = CONFIG_DIR / 'wezterm' / 'color.lua'

def get_user_confirmation():
    """Prompt the user for confirmation."""
    while True:
        user_input = input("\033[31m" + "Warning: " + "\033[0m" + "The script will close Zellij if it is running. Do you want to continue? (y/n): ").strip().lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def load_color_schemes():
    """Load the color schemes from the TOML file."""
    try:
        with open(COLOR_SCHEMES_FILE, 'r') as file:
            return toml.load(file)
    except FileNotFoundError:
        print(f"Error: {COLOR_SCHEMES_FILE} not found.")
        exit(1)
    except toml.TomlDecodeError:
        print(f"Error: Failed to decode {COLOR_SCHEMES_FILE}.")
        exit(1)

def show_available_schemes(schemes):
    """Display the available color schemes."""
    print("\033[94m" + "Available schemes:" + "\033[0m")
    for i, scheme in enumerate(schemes):
        print(f"[{i}] {scheme}")

def select_scheme(schemes):
    """Prompt the user to select a color scheme."""
    while True:
        current_scheme = input("\033[94m" + "Please enter the color scheme number or 'x' to exit: " + "\033[0m")
        if current_scheme.lower() == 'x':
            print("Exiting...")
            exit(0)
        try:
            current_scheme = int(current_scheme)
            if 0 <= current_scheme < len(schemes):
                return current_scheme
            else:
                print(f"\033[31mInvalid input. The number must be between 0 and {len(schemes) - 1}.\033[0m")
        except ValueError:
            print("\033[31mInvalid input. Please enter an integer.\033[0m")

def is_installed(program):
    """Check if a program is installed."""
    try:
        result = subprocess.run(['flatpak', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if program in result.stdout:
            return True
        elif shutil.which(program) is not None:
            return True 
        else:
            return False
    except FileNotFoundError:
        print("Flatpak is not installed on this system.")

def set_color_scheme():
    """Main function to set the color schemes."""
    print("\033[32m" + "Info: " + "\033[0m" + "This script will change the color schemes for Zellij, WezTerm, and Alacritty.")

    if not get_user_confirmation():
        print("Operation cancelled by the user.")
        return

    data = load_color_schemes()
    schemes = list(data['schemes'].keys())
    show_available_schemes(schemes)
    current_scheme = select_scheme(schemes)
    scheme_data = data['schemes'][schemes[current_scheme]]
    
    # Checks if Alacritty is installed
    if is_installed('alacritty'):
        set_alacritty_color_scheme(ALACRITTY_THEME_FILE, scheme_data)

    # Checks if Wezterm is installed
    if is_installed('wezterm'):
        set_wezterm_color_scheme(WEZTERM_THEME_FILE, scheme_data)

    # Checks if Zellij is installed
    if is_installed('zellij'):
        set_zellij_color_scheme(ZELLIJ_THEME_FILE, scheme_data)
        
if __name__ == "__main__":
    set_color_scheme()