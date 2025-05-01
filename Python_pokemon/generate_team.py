import argparse
import requests
import random
from pydantic import BaseModel
import json

# Set up argparse
parser = argparse.ArgumentParser(description="Generate a Pokémon team by type.")
parser.add_argument("--type", default=None, help="Only include Pokémon with this type.")
args = parser.parse_args()
selected_type = args.type.lower() if args.type else None

# Define your model
class Pokemon(BaseModel):
    name: str
    types: list[str]
    hp_stat: int
    ability_names: list[str]

team = []

# Keep fetching Pokémon until we have 6 of the desired type (or any type if none specified)
while len(team) < 6:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random.randrange(1, 150)}/")
    data = response.json()

    name = data["name"]
    hp_stat = next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "hp")
    types = [type_entry["type"]["name"] for type_entry in data["types"]]
    ability_names = [ability["ability"]["name"] for ability in data["abilities"]]

    # Check type condition if --type is used
    if selected_type and selected_type not in types:
        continue  # Skip if the Pokémon isn't of the desired type

    temp_poke = Pokemon(
        name=name,
        types=types,
        hp_stat=hp_stat,
        ability_names=ability_names
    )

    team.append(temp_poke)

# Convert team to serializable format
team_data = [poke.model_dump() for poke in team]

# Sort by HP
def get_pokemon(element):
    return element['hp_stat']

team_data.sort(key=get_pokemon)

# Save to file
with open("Python_pokemon/team.json", "w") as file:
    json.dump(team_data, file, indent=2)

print(f"Generated team: {[poke.name for poke in team]}")

# Random battle between 2 team members
fighters = random.sample(team, 2)
print(f"Generated fighters: {[poke.name for poke in fighters]}")

if fighters[0].hp_stat > fighters[1].hp_stat:
    print(f"{fighters[0].name} is the Winner, with {fighters[0].hp_stat - fighters[1].hp_stat} health left")
elif fighters[0].hp_stat == fighters[1].hp_stat:
    print(f"It's a draw between {fighters[0].name} and {fighters[1].name}")
else:
    print(f"{fighters[1].name} is the Winner, with {fighters[1].hp_stat - fighters[0].hp_stat} health left")
