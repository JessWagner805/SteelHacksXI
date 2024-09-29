import json
with open('chatgpt_output.json','r') as file:
    json_string = json.load(file)

# Load the JSON string into a Python dictionary
data = json.loads(json_string)

# Function to print categorized output
def pretty_print_json(data):
    # Print Weapons
    print("\nWeapons:")
    for weapon in data["Weapons"]:
        print(f"  {weapon}")
    
    # Print Spells and Incantations
    print("\nSpells and Incantations:")
    for spell in data["Spells and Incantations"]:
        print(f"  {spell}")
    
    # Print Armor
    print("\nArmor:")
    for armor in data["Armor"]:
        print(f"  {armor}")
    
    # Print Items
    print("\nItems:")
    for item in data["Items"]:
        print(f"  {item}")
    
    # Print Strategy
    print("\nStrategy:")
    print(f"  {data['Strategy']}")

# Call the function to print the categorized output
pretty_print_json(data)
