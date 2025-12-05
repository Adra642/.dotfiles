"""Logging configuration for the color scheme selector."""

import logging
import sys


def setup_logger(
    name: str = "color_selector", level: int = logging.INFO
) -> logging.Logger:
    """
    Set up and configure the logger.

    Args:
        name: Logger name
        level: Logging level (default: INFO)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding multiple handlers if logger already exists
    if logger.handlers:
        return logger

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


# Create default logger instance
logger = setup_logger()
