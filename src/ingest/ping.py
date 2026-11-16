"""temp script for testing out pokeapi"""

import httpx2

if __name__ == "__main__":
    response = httpx2.get("https://pokeapi.co/api/v2/pokemon/rayquaza")
    print(response.status_code)

    json = response.json()
    print(json)
