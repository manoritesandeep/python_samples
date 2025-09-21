import requests

sample_url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(sample_url)
total_records = response.json().get("count")

print(f"Total records: {total_records}")

all_pokemon = []

for i in range(0, total_records, 20):
    paginated_url = f"{sample_url}?offset={i}&limit=20"
    response = requests.get(paginated_url)
    data = response.json()
    all_pokemon.extend(data.get("results", []))
    # all_data.append(data)

print(f"Length of all data: {len(all_pokemon)}")

# Total records: 1302
# Length of all data: 1302