# 🎮 Pokémon Team Generator Task

In this fun backend task, you'll use the **PokéAPI** (https://pokeapi.co/) to build a **Pokémon Team Generator**. You'll fetch Pokémon data over HTTP, process JSON, and output a custom team roster.

---

## 🚀 Task Goal

Write a Python script (`generate_team.py`) that:

1. **Fetches** a list of Pokémon species from the PokéAPI.
   ```python
   response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=150")
   data = response.json()  # data['results'] is a list of name/url pairs
   ```
2. **Selects** 6 random Pokémon from that list.
3. For each selected Pokémon, **fetch** its detailed data:
   ```python
   detail = requests.get(pokemon['url']).json()
   # e.g., detail['types'], detail['stats'], detail['abilities']
   ```
4. **Builds** a `team` list of dicts containing:
   - `name`: Pokémon name
   - `types`: list of type names
   - `hp_stat`: the HP base stat
   - `ability_names`: list of ability names
5. **Writes** the team to `team.json` with pretty JSON formatting:
   ```json
   [
     {
       "name": "pikachu",
       "types": ["electric"],
       "hp_stat": 35,
       "ability_names": ["static", "lightning-rod"]
     },
     ...
   ]
   ```
6. **Prints** a summary to the console:
   > "Generated team: Pikachu (Electric), Bulbasaur (Grass, Poison), ..."

---

## 📦 Starter Hints

- Use the `requests` library:
  ```python
  import requests
  ```
- Use Python’s built-in `random.sample` to pick 6 unique entries:
  ```python
  import random
  team_choices = random.sample(data['results'], 6)
  ```
- Extract nested JSON fields for types and stats.
- Handle HTTP errors (check `response.status_code`).

---

## 🌟 Stretch Goals

1. **Filter by Type**: Add a `--type` CLI flag (using `argparse`) to only choose Pokémon matching a given type (e.g., `--type=water`).
2. **Stat-Based Sorting**: After fetching stats, sort your team by HP descending and print the highest-HP Pokémon first.
3. **Battle Simulator**: Prompt the user to pick two Pokémon from the generated team and simulate a simple "battle" by comparing their total base stats; declare the winner.

---

## 💡 Tips

- Read the PokéAPI docs: https://pokeapi.co/docs/v2
- Work in small steps: fetch the list, then fetch details for one Pokémon.
- Print intermediate data (`print(detail)`) to understand the structure.

Have fun catching ‘em all! 🐾

