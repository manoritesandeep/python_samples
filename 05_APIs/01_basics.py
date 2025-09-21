import requests

sample_url = "https://pokeapi.co/api/v2/pokemon/"

# response = requests.get(sample_url)
# data = response.json()

def get_pokemon(url):
  response = requests.get(url)
  print(f"Response status code: {response.status_code}")
  return response.json()

def get_pokemon_list(url):
  response = requests.get(url)
  return response.json()['results']

print(get_pokemon(sample_url))
# print("\n")
# print(get_pokemon_list(sample_url))

