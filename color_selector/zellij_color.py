import subprocess


def write_kdl_file(file_path, color_string):
    """Save the Zellij color scheme to a KDL file."""
    try:
        with open(file_path, "w") as file:
            file.write(color_string)
    except IOError:
        print(f"Error: Failed to write to {file_path}.")
        exit(1)


def map_color_scheme(scheme_data):
    """Map the color scheme to Zellij format."""
    primary_colors = scheme_data["colors"]["primary"]
    normal_colors = scheme_data["colors"]["normal"]

    color_mappings = {
        "fg": "foreground",
        "bg": "background",
        "orange": "red",
    }

    color_properties = [
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
        if prop in [
            "fg",
            "bg",
        ]:
            color_string += f'      {prop} "{primary_colors[color_mappings[prop]]}"\n'
        elif prop in ["orange"]:
            color_string += f'      {prop} "{normal_colors[color_mappings[prop]]}"\n'
        else:
            color_string += f'      {prop} "{normal_colors[prop]}"\n'
    color_string += "   }\n}"

    return color_string


def set_zellij_color_scheme(file_path, scheme_data):
    """Set the Zellij color scheme."""
    color_scheme = map_color_scheme(scheme_data)
    write_kdl_file(file_path, color_scheme)
    # Kill all Zellij sessions to apply new color scheme
    subprocess.run(
        ["zellij", "ka", "-y"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
