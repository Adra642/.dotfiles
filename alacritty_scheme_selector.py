import os
import json
import toml
import time

# Load the JSON data from the file
home = os.environ['HOME']
with open(f'{home}/.config/alacritty/color_schemes.json', 'r') as file:
    data = json.load(file)

# Get the keys from the 'index' dictionary and add them to an array
schemes = list(data['schemes'].keys())

# Show the available schemes
print("\033[94m" + "Available schemes:" + "\033[0m")
for i, scheme in enumerate(schemes):
    print(f"[{i}] {scheme}")

print("\033[31m" + "Warning: " + "\033[0m" + "This script will close Zellij if it is running.")
# Validate the input
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

scheme_data = data['schemes'][schemes[current_scheme]]
toml_string = toml.dumps(scheme_data)

with open(f'{home}/.config/alacritty/current_scheme.toml', 'w') as file:
    file.write(toml_string)

# Verificar si Zellij está instalado
zellij_installed = os.system('which zellij > /dev/null 2>&1')

if zellij_installed == 0:
    primary_colors = scheme_data['colors']['primary']
    normal_colors = scheme_data['colors']['normal']

    color_properties = [
        'fg', 'bg', 'red', 'green', 'yellow', 'blue', 'cyan', 'magenta', 'orange', 'black', 'white'
    ]

    color_values = {
        'fg': primary_colors['foreground'],
        'bg': primary_colors['background'],
        'red': normal_colors['red'],
        'green': normal_colors['green'],
        'yellow': normal_colors['yellow'],
        'blue': normal_colors['blue'],
        'cyan': normal_colors['cyan'],
        'magenta': normal_colors['magenta'],
        'orange': normal_colors['red'],
        'black': normal_colors['black'],
        'white': normal_colors['white'],
    }

    color_string = "themes {\n   default {\n"
    for prop in color_properties:
        color_string += f"      {prop} \"{color_values[prop]}\"\n"
    color_string += "   }\n}"

    # Guardar el archivo KDL
    with open(f'{home}/.config/zellij/theme/scheme.kdl', 'w') as file:
        file.write(color_string)
    
    os.system('zellij ka -y > /dev/null 2>&1')
