"""Alacritty color scheme handler.

This module handles the conversion and application of color schemes
for the Alacritty terminal emulator.
"""

import sys
import toml
from pathlib import Path
from typing import Dict, Any

from logger import logger
from constants import Messages, ExitCodes


def write_toml_file(file_path: Path, content: str) -> None:
    """
    Save the Alacritty color scheme to a TOML file.

    Args:
        file_path: Path to the output file
        content: TOML content to write

    Raises:
        SystemExit: If file write fails
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
        logger.debug(f"Wrote Alacritty config to {file_path}")
    except IOError as e:
        logger.error(f"{Messages.write_error(str(file_path))}: {e}")
        sys.exit(ExitCodes.ERROR_IO)


def convert_scheme_to_toml(scheme_data: Dict[str, Any]) -> str:
    """
    Convert color scheme data to TOML format.

    Args:
        scheme_data: Dictionary containing color scheme data

    Returns:
        TOML-formatted string
    """
    return toml.dumps(scheme_data)


def set_alacritty_color_scheme(file_path: Path, scheme_data: Dict[str, Any]) -> None:
    """
    Set the Alacritty color scheme.

    Args:
        file_path: Path to the Alacritty theme file
        scheme_data: Color scheme data dictionary
    """
    color_scheme = convert_scheme_to_toml(scheme_data)
    write_toml_file(file_path, color_scheme)
