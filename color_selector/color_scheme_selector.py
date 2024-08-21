import os
import toml
from pathlib import Path
import shutil
import subprocess

from zellij_color import set_zellij_color_scheme
from wezterm_color import set_wezterm_color_scheme

CONFIG_DIR = Path(os.environ['HOME']) / '.config'
COLOR_SCHEMES_FILE = CONFIG_DIR / 'color_selector' / 'color_schemes.toml'
ALACRITTY_THEME_FILE = CONFIG_DIR / 'alacritty' / 'current_scheme.toml'
ZELLIJ_THEME_FILE = CONFIG_DIR / 'zellij' / 'theme' / 'scheme.kdl'
WEZTERM_THEME_FILE = CONFIG_DIR / 'wezterm' / 'color.lua'

def load_schemes():
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

def show_schemes(schemes):
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

def save_toml_file(scheme_data):
    """Save the selected color scheme to a TOML file."""
    try:
        toml_string = toml.dumps(scheme_data)
        with open(ALACRITTY_THEME_FILE, 'w') as file:
            file.write(toml_string)
    except IOError:
        print(f"Error: Failed to write to {ALACRITTY_THEME_FILE}.")
        exit(1)

def is_zellij_installed():
    """Check if Zellij is installed."""
    return shutil.which('zellij') is not None

def is_wezterm_installed():
    """Check if WezTerm is installed as a Flatpak."""
    try:
        result = subprocess.run(['flatpak', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if 'WezTerm' in result.stdout:
            return True
        elif shutil.which('wezterm') is not None:
            return True 
        else:
            return False
    except FileNotFoundError:
        print("Flatpak is not installed on this system.")

def get_user_confirmation():
    """Prompt the user for confirmation."""
    while True:
        user_input = input("\033[31m" + "Warning: " + "\033[0m" + "The script will close Zellij if it is running. Do you want to continue? (y/n): ").strip().lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def set_color_schemes():
    """Main function to set the color schemes."""
    print("\033[32m" + "Info: " + "\033[0m" + "This script will change the color schemes for Zellij, WezTerm, and Alacritty.")

    if not get_user_confirmation():
        print("Operation cancelled by the user.")
        return

    data = load_schemes()
    schemes = list(data['schemes'].keys())
    show_schemes(schemes)
    current_scheme = select_scheme(schemes)
    scheme_data = data['schemes'][schemes[current_scheme]]
    save_toml_file(scheme_data)

    # if wezterm is installed
    if is_wezterm_installed():
        set_wezterm_color_scheme(scheme_data, WEZTERM_THEME_FILE)

    # if zellij is installed
    if is_zellij_installed():
        set_zellij_color_scheme(scheme_data, ZELLIJ_THEME_FILE)
        
if __name__ == "__main__":
    set_color_schemes()