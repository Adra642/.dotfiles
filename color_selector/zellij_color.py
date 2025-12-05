"""Zellij color scheme handler.

This module handles the conversion and application of color schemes
for the Zellij terminal multiplexer.
"""

import sys
import subprocess
from pathlib import Path
from typing import Dict, Any, List

from logger import logger
from constants import Messages, ExitCodes


def write_kdl_file(file_path: Path, color_string: str) -> None:
    """
    Save the Zellij color scheme to a KDL file.

    Args:
        file_path: Path to the output file
        color_string: KDL content to write

    Raises:
        SystemExit: If file write fails
    """
    try:
        with open(file_path, "w") as file:
            file.write(color_string)
        logger.debug(f"Wrote Zellij config to {file_path}")
    except IOError as e:
        logger.error(f"{Messages.write_error(str(file_path))}: {e}")
        sys.exit(ExitCodes.ERROR_IO)


def map_color_scheme(scheme_data: Dict[str, Any]) -> str:
    """
    Map the color scheme to Zellij KDL format.

    Args:
        scheme_data: Dictionary containing color scheme data

    Returns:
        KDL-formatted color scheme string

    Raises:
        KeyError: If required color keys are missing
        SystemExit: If color data is invalid
    """
    try:
        primary_colors = scheme_data["colors"]["primary"]
        normal_colors = scheme_data["colors"]["normal"]
    except KeyError as e:
        logger.error(f"Missing required color key in scheme data: {e}")
        sys.exit(ExitCodes.ERROR_INVALID_DATA)

    color_mappings: Dict[str, str] = {
        "fg": "foreground",
        "bg": "background",
        "orange": "red",
    }

    color_properties: List[str] = [
        "fg",
        "bg",
        "red",
        "green",
        "yellow",
        "blue",
        "cyan",
        "magenta",
        "orange",
        "black",
        "white",
    ]

    color_string = "themes {\n   default {\n"
    for prop in color_properties:
        if prop in ["fg", "bg"]:
            color_string += f'      {prop} "{primary_colors[color_mappings[prop]]}"\n'
        elif prop == "orange":
            color_string += f'      {prop} "{normal_colors[color_mappings[prop]]}"\n'
        else:
            color_string += f'      {prop} "{normal_colors[prop]}"\n'
    color_string += "   }\n}"

    return color_string


def kill_zellij_sessions() -> None:
    """
    Kill all Zellij sessions to apply the new color scheme.

    This is necessary because Zellij needs to be restarted to pick up
    the new color scheme configuration.
    """
    try:
        result = subprocess.run(
            ["zellij", "ka", "-y"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode == 0:
            logger.debug("Killed Zellij sessions successfully")
        else:
            logger.warning(f"Zellij kill command returned code {result.returncode}")
    except FileNotFoundError:
        logger.warning("Zellij command not found, skipping session kill")
    except Exception as e:
        logger.warning(f"Failed to kill Zellij sessions: {e}")


def set_zellij_color_scheme(file_path: Path, scheme_data: Dict[str, Any]) -> None:
    """
    Set the Zellij color scheme.

    Args:
        file_path: Path to the Zellij theme file
        scheme_data: Color scheme data dictionary
    """
    color_scheme = map_color_scheme(scheme_data)
    write_kdl_file(file_path, color_scheme)
    kill_zellij_sessions()
