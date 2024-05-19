import json
import toml

# Open the JSON file
with open('color_schemes.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Get the keys from the 'index' dictionary and add them to an array
schemes = list(data['schemes'].keys())

# Show the available schemes
print("\033[92m" + "Available schemes:" + "\033[0m")
for i, scheme in enumerate(schemes):
    print(f"[{i}] {scheme}")

# Validate the input
while True:
    current_scheme = input("Please enter the color scheme number: ")
    try:
        current_scheme = int(current_scheme)
    except ValueError:
        print("\033[91m" + "Invalid input. Please enter an integer." + "\033[0m")
        continue
    if current_scheme >= len(schemes):
        print("\033[91m" + "Invalid input. The number must be less than " + str(len(schemes)) + "\033[0m")
        continue
    break

scheme_data = data['schemes'][schemes[current_scheme]]
toml_string = toml.dumps(scheme_data)

with open('current_scheme.toml', 'w') as file:
    file.write(toml_string)