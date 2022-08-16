#!/url/bin/env python3

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

#send a get request
resp= requests.get(url)

pokedex=resp.json()

print(pokedex["sprintes"]["front_default"])


