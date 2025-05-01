import requests
import random
from pydantic import BaseModel
import json

class Pokemon(BaseModel):
    name: str
    types: list[str]
    hp_stat: int
    ability_names: list[str]

team = []

for _ in range(6):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random.randrange(1, 150)}/")
    data = response.json()

    # Extract values
    name = data["name"]
    hp_stat = next(stat["base_stat"] for stat in data["stats"] if stat["stat"]["name"] == "hp")
    types = [type_entry["type"]["name"] for type_entry in data["types"]]
    ability_names = [ability["ability"]["name"] for ability in data["abilities"]]

    # Initialize with all required fields
    temp_poke = Pokemon(
        name=name,
        types=types,
        hp_stat=hp_stat,
        ability_names=ability_names
    )

    team.append(temp_poke)

team_data = [poke.model_dump() for poke in team]

#Sort pokemons based on hp_stat
def get_pokemon(element):
    return element['hp_stat']

team_data.sort(reverse=False, key=get_pokemon)

# Save to a file
with open("Python pokemon/team.json", "w") as file:
    json.dump(team_data, file, indent=2)

print(f"Generated team: {[poke.name for poke in team]}")