"""Color scheme selector for terminal applications.

This script allows users to select and apply color schemes across
Zellij, WezTerm, and Alacritty terminal applications.
"""

import os
import sys
import toml
from pathlib import Path
import shutil
import subprocess
from typing import Dict, List, Any

from zellij_color import set_zellij_color_scheme
from wezterm_color import set_wezterm_color_scheme
from alacritty_color import set_alacritty_color_scheme
from constants import Colors, Messages, ExitCodes
from logger import logger

CONFIG_DIR = Path(os.environ["HOME"]) / ".config"
DOTFILES_DIR = Path(os.environ["HOME"]) / ".dotfiles"
COLOR_SCHEMES_DIR = DOTFILES_DIR / "color_selector" / "schemes"
ALACRITTY_THEME_FILE = CONFIG_DIR / "alacritty" / "current_scheme.toml"
ZELLIJ_THEME_FILE = CONFIG_DIR / "zellij" / "themes" / "scheme.kdl"
WEZTERM_THEME_FILE = CONFIG_DIR / "wezterm" / "color.lua"


def get_user_confirmation() -> bool:
    """
    Prompt the user for confirmation.

    Returns:
        True if user confirms, False otherwise
    """
    while True:
        user_input = (
            input(f"{Colors.RED}Warning: {Colors.RESET}{Messages.WARNING_ZELLIJ}")
            .strip()
            .lower()
        )
        if user_input in ["y", "n"]:
            return user_input == "y"
        print(Messages.INVALID_YN)


def list_available_schemes() -> List[str]:
    """
    List available color scheme names from the schemes directory.

    This function only reads filenames, not file contents, for efficiency.

    Returns:
        Sorted list of scheme names (without .toml extension)

    Raises:
        SystemExit: If directory not found or no schemes available
    """
    schemes_dir = COLOR_SCHEMES_DIR

    if not schemes_dir.exists():
        logger.error(f"Schemes directory not found: {schemes_dir}")
        sys.exit(ExitCodes.ERROR_FILE_NOT_FOUND)

    # Get all .toml files and extract names (stems)
    scheme_files = list(schemes_dir.glob("*.toml"))

    if not scheme_files:
        logger.error(f"No color schemes found in {schemes_dir}")
        sys.exit(ExitCodes.ERROR_INVALID_DATA)

    scheme_names = sorted([f.stem for f in scheme_files])
    logger.debug(f"Found {len(scheme_names)} scheme(s): {', '.join(scheme_names)}")

    return scheme_names


def load_scheme(scheme_name: str) -> Dict[str, Any]:
    """
    Load a specific color scheme by name.

    Args:
        scheme_name: Name of the scheme to load (without .toml extension)

    Returns:
        Dictionary containing the color scheme data

    Raises:
        SystemExit: If scheme file not found or invalid
    """
    scheme_file = COLOR_SCHEMES_DIR / f"{scheme_name}.toml"

    if not scheme_file.exists():
        logger.error(f"Scheme file not found: {scheme_file}")
        sys.exit(ExitCodes.ERROR_FILE_NOT_FOUND)

    try:
        with open(scheme_file, "r") as f:
            scheme_data = toml.load(f)
            logger.info(f"Loaded scheme: {scheme_name}")
            return scheme_data
    except toml.TomlDecodeError as e:
        logger.error(f"Failed to parse {scheme_file.name}: {e}")
        sys.exit(ExitCodes.ERROR_DECODE)
    except Exception as e:
        logger.error(f"Error loading {scheme_file.name}: {e}")
        sys.exit(ExitCodes.ERROR_IO)


def show_available_schemes(schemes: List[str]) -> None:
    """
    Display the available color schemes.

    Args:
        schemes: List of scheme names
    """
    print(f"{Colors.BLUE}{Messages.AVAILABLE_SCHEMES}{Colors.RESET}")
    for i, scheme in enumerate(schemes):
        print(f"[{i}] {scheme}")


def select_scheme(schemes: List[str]) -> int:
    """
    Prompt the user to select a color scheme.

    Args:
        schemes: List of available scheme names

    Returns:
        Index of the selected scheme

    Raises:
        SystemExit: If user chooses to exit
    """
    while True:
        current_scheme = input(
            f"{Colors.BLUE}{Messages.PROMPT_SCHEME_NUMBER}{Colors.RESET}"
        )
        if current_scheme.lower() == "x":
            logger.info(Messages.EXITING)
            sys.exit(ExitCodes.SUCCESS)
        try:
            current_scheme_idx = int(current_scheme)
            if 0 <= current_scheme_idx < len(schemes):
                logger.info(f"Selected scheme: {schemes[current_scheme_idx]}")
                return current_scheme_idx
            else:
                print(
                    f"{Colors.RED}{Messages.invalid_range(len(schemes) - 1)}{Colors.RESET}"
                )
        except ValueError:
            print(f"{Colors.RED}{Messages.INVALID_INTEGER}{Colors.RESET}")


def is_installed(program: str) -> bool:
    """
    Check if a program is installed.

    Args:
        program: Name of the program to check

    Returns:
        True if program is installed, False otherwise
    """
    # Check system PATH first (most common case)
    if shutil.which(program) is not None:
        logger.debug(f"{program} found in system PATH")
        return True

    # Check flatpak if available
    try:
        result = subprocess.run(
            ["flatpak", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if program in result.stdout:
            logger.debug(f"{program} found in flatpak")
            return True
        return False
    except FileNotFoundError:
        # Flatpak not installed, already checked system PATH
        logger.debug("Flatpak not available")
        return False


def apply_color_schemes(scheme_data: Dict[str, Any]) -> None:
    """
    Apply color scheme to all installed terminal applications.

    Args:
        scheme_data: Color scheme data dictionary
    """
    applied_count = 0

    # Apply to Alacritty
    if is_installed("alacritty"):
        try:
            set_alacritty_color_scheme(ALACRITTY_THEME_FILE, scheme_data)
            logger.info("Applied color scheme to Alacritty")
            applied_count += 1
        except Exception as e:
            logger.error(f"Failed to apply scheme to Alacritty: {e}")

    # Apply to Wezterm
    if is_installed("wezterm"):
        try:
            set_wezterm_color_scheme(WEZTERM_THEME_FILE, scheme_data)
            logger.info("Applied color scheme to WezTerm")
            applied_count += 1
        except Exception as e:
            logger.error(f"Failed to apply scheme to WezTerm: {e}")

    # Apply to Zellij
    if is_installed("zellij"):
        try:
            set_zellij_color_scheme(ZELLIJ_THEME_FILE, scheme_data)
            logger.info("Applied color scheme to Zellij")
            applied_count += 1
        except Exception as e:
            logger.error(f"Failed to apply scheme to Zellij: {e}")

    if applied_count == 0:
        logger.warning("No supported terminal applications found")
    else:
        logger.info(
            f"Successfully applied color scheme to {applied_count} application(s)"
        )


def set_color_scheme() -> None:
    """Main function to set the color schemes."""
    print(f"{Colors.GREEN}Info: {Colors.RESET}{Messages.INFO_HEADER}")

    if not get_user_confirmation():
        logger.info(Messages.OPERATION_CANCELLED)
        return

    # List available schemes (fast - just filenames)
    schemes = list_available_schemes()

    # Show schemes and let user select
    show_available_schemes(schemes)
    current_scheme_idx = select_scheme(schemes)
    scheme_name = schemes[current_scheme_idx]

    # Load only the selected scheme (lazy loading)
    scheme_data = load_scheme(scheme_name)

    # Apply the scheme
    apply_color_schemes(scheme_data)


if __name__ == "__main__":
    try:
        set_color_scheme()
    except KeyboardInterrupt:
        logger.info("\nOperation interrupted by user")
        sys.exit(ExitCodes.SUCCESS)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
