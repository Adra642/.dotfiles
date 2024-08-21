import toml

def write_toml_file(file_path, content):
    """Save the Alacritty color scheme to a toml file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError:
        print(f"Error: Failed to write to {file_path}.")
        exit(1)

def change_to_toml(scheme_data):
    return toml.dumps(scheme_data)


def set_alacritty_color_scheme(file_path,scheme_data ):
    """Set the Alacritty color scheme."""
    color_scheme = change_to_toml(scheme_data)
    write_toml_file(file_path, color_scheme)