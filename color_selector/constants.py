"""Constants for the color scheme selector."""


# ANSI Color Codes for Terminal Output
class Colors:
    """ANSI escape codes for colored terminal output."""

    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[94m"
    RESET = "\033[0m"


# Application Messages
class Messages:
    """User-facing messages."""

    INFO_HEADER = (
        "This script will change the color schemes for Zellij, WezTerm, and Alacritty."
    )
    WARNING_ZELLIJ = "The script will close Zellij if it is running. Do you want to continue? (y/n): "
    OPERATION_CANCELLED = "Operation cancelled by the user."
    EXITING = "Exiting..."
    AVAILABLE_SCHEMES = "Available schemes:"
    PROMPT_SCHEME_NUMBER = "Please enter the color scheme number or 'x' to exit: "
    INVALID_YN = "Invalid input. Please enter 'y' or 'n'."
    INVALID_INTEGER = "Invalid input. Please enter an integer."

    @staticmethod
    def invalid_range(max_val: int) -> str:
        """Generate invalid range message."""
        return f"Invalid input. The number must be between 0 and {max_val}."

    @staticmethod
    def file_not_found(filepath: str) -> str:
        """Generate file not found message."""
        return f"Error: {filepath} not found."

    @staticmethod
    def decode_error(filepath: str) -> str:
        """Generate decode error message."""
        return f"Error: Failed to decode {filepath}."

    @staticmethod
    def write_error(filepath: str) -> str:
        """Generate write error message."""
        return f"Error: Failed to write to {filepath}."


# Exit Codes
class ExitCodes:
    """Standard exit codes."""

    SUCCESS = 0
    ERROR_FILE_NOT_FOUND = 1
    ERROR_DECODE = 1
    ERROR_IO = 1
    ERROR_INVALID_DATA = 2
