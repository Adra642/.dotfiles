import os
import json
import toml

# Load the JSON data from the file
def load_schemes():
    home = os.environ['HOME']
    with open(f'{home}/.config/color_schemes.json', 'r') as file:
        data = json.load(file)
    return data

# Show the available schemes
def show_schemes(schemes):
    print("\033[94m" + "Available schemes:" + "\033[0m")
    for i, scheme in enumerate(schemes):
        print(f"[{i}] {scheme}")

# Validate the input
def select_scheme(schemes):
    while True:
        current_scheme = input("\033[94m" + "Please enter the color scheme number or 'x' to exit: " + "\033[0m")
        if current_scheme.lower() == 'x':
            print("Exiting...")
            exit(0)
        try:
            current_scheme = int(current_scheme)
        except ValueError:
            print("\033[31m" + "Invalid input. Please enter an integer." + "\033[0m")
            continue
        if current_scheme >= len(schemes):
            print("\033[31m" + "Invalid input. The number must be less than " + str(len(schemes)) + "\033[0m")
            continue
        break
    return current_scheme

# Save the TOML file
def save_toml_file(scheme_data):
    home = os.environ['HOME']
    toml_string = toml.dumps(scheme_data)
    with open(f'{home}/.config/alacritty/current_scheme.toml', 'w') as file:
        file.write(toml_string)

def is_zellij_installed():
    return os.system('which zellij > /dev/null 2>&1') == 0

def map_color_scheme(scheme_data):
    primary_colors = scheme_data['colors']['primary']
    normal_colors = scheme_data['colors']['normal']

    color_mappings = {
        'fg': 'foreground',
        'bg': 'background',
        'orange': 'red',
    }

    color_properties = [
        'fg', 'bg', 'red', 'green', 'yellow', 'blue', 'cyan', 'magenta', 'orange', 'black', 'white'
    ]

    color_string = "themes {\n   default {\n"
    for prop in color_properties:
        if prop in ['fg', 'bg',]:
            color_string += f"      {prop} \"{primary_colors[color_mappings[prop]]}\"\n"
        elif prop in ['orange']:
            color_string += f"      {prop} \"{normal_colors[color_mappings[prop]]}\"\n"
        else:
            color_string += f"      {prop} \"{normal_colors[prop]}\"\n"
    color_string += "   }\n}"

    return color_string

def save_kdl_file(color_string):
    home = os.environ['HOME']
    with open(f'{home}/.config/zellij/theme/scheme.kdl', 'w') as file:
        file.write(color_string)   

def set_zellij_color_scheme(scheme_data):
    color_string = map_color_scheme(scheme_data)
    save_kdl_file(color_string)
    os.system('zellij ka -y > /dev/null 2>&1')

def get_user_confirmation():
    while True:
        user_input = input("\033[31m" + "Warning: " + "\033[0m" + "The script will close Zellij if it is running. Do you want to continue? (y/n): ").strip().lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def set_color_schemes():
    print("\033[32m" + "Info: " + "\033[0m" + "This script will change the color schemes for Zellij, WezTerm, and Alacritty.")

    if not get_user_confirmation():
        print("Operation cancelled by the user.")
        return

    data = load_schemes()
    schemes = list(data['schemes'].keys())
    show_schemes(schemes)
    current_scheme = select_scheme(schemes)
    scheme_data = data['schemes'][schemes[current_scheme]]
    print(scheme_data)
    save_toml_file(scheme_data)

    if is_zellij_installed():
        set_zellij_color_scheme(scheme_data)

set_color_schemes()