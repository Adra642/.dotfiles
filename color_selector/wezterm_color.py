"""WezTerm color scheme handler.

This module handles the conversion and application of color schemes
for the WezTerm terminal emulator.
"""

import sys
from pathlib import Path
from typing import Dict, Any

from logger import logger
from constants import Messages, ExitCodes


def write_lua_file(file_path: Path, content: str) -> None:
    """
    Save the WezTerm color scheme to a Lua file.

    Args:
        file_path: Path to the output file
        content: Lua code content to write

    Raises:
        SystemExit: If file write fails
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
        logger.debug(f"Wrote WezTerm config to {file_path}")
    except IOError as e:
        logger.error(f"{Messages.write_error(str(file_path))}: {e}")
        sys.exit(ExitCodes.ERROR_IO)


def extract_colors(scheme_data: Dict[str, Any]) -> str:
    """
    Extract colors from the scheme data dictionary and generate Lua code.

    Args:
        scheme_data: Dictionary containing color scheme data

    Returns:
        Lua code string for WezTerm configuration

    Raises:
        KeyError: If required color keys are missing
        SystemExit: If color data is invalid
    """
    try:
        colors = scheme_data["colors"]
        primary = colors["primary"]
        normal = colors["normal"]
        bright = colors["bright"]
        selection = colors["selection"]
        cursor = colors["cursor"]
    except KeyError as e:
        logger.error(f"Missing required color key in scheme data: {e}")
        sys.exit(ExitCodes.ERROR_INVALID_DATA)

    color_string = "local wezterm = require 'wezterm'\n"
    color_string += "local module = {}\n"
    color_string += "function module.set_color_scheme(config)\n"
    color_string += f"""
    config.colors = {{
        background = "{primary["background"]}",
        foreground = "{primary["foreground"]}",

        ansi = {{ 
            "{normal["black"]}", 
            "{normal["red"]}", 
            "{normal["green"]}", 
            "{normal["yellow"]}", 
            "{normal["blue"]}", 
            "{normal["magenta"]}", 
            "{normal["cyan"]}", 
            "{normal["white"]}" 
        }},
        brights = {{ 
            "{bright["black"]}", 
            "{bright["red"]}", 
            "{bright["green"]}", 
            "{bright["yellow"]}", 
            "{bright["blue"]}", 
            "{bright["magenta"]}", 
            "{bright["cyan"]}", 
            "{bright["white"]}" 
        }},

        selection_bg = "{selection["background"]}",
        selection_fg = "{selection["foreground"]}",

        cursor_bg = "{cursor["cursor"]}",
        cursor_border = "{cursor["cursor"]}",
    }}    
    """
    color_string += "\nend"
    color_string += "\nreturn module"
    return color_string


def set_wezterm_color_scheme(file_path: Path, scheme_data: Dict[str, Any]) -> None:
    """
    Set the WezTerm color scheme.

    Args:
        file_path: Path to the WezTerm color configuration file
        scheme_data: Color scheme data dictionary
    """
    color_scheme = extract_colors(scheme_data)
    write_lua_file(file_path, color_scheme)
