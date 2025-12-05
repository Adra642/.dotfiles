def write_lua_file(file_path, content):
    """Save the Wezterm color scheme to a Lua file."""
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except IOError:
        print(f"Error: Failed to write to {file_path}.")
        exit(1)


def extract_colors(scheme_data):
    """Extract colors from the scheme data dictionary."""
    colors = scheme_data["colors"]
    primary = colors["primary"]
    normal = colors["normal"]
    bright = colors["bright"]
    selection = colors["selection"]
    cursor = colors["cursor"]

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


def set_wezterm_color_scheme(file_path, scheme_data):
    """Set the Wezterm color scheme."""
    color_scheme = extract_colors(scheme_data)
    write_lua_file(file_path, color_scheme)
