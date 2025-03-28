import asyncio
import requests

BASE_URL = "https://world.openfoodfacts.org/api.v0/product"

def get_food_by_barcode(barcode):
    response = requests.get(f"{BASE_URL}/{barcode}.json")
    if response.status_code == 200:
        return response.json()
    return None

# Asynchronous version to handle multiple food query request concurrently from users.
async def async_search_foods(query):
    response = await asyncio.to_thread(
        requests.get, f"https://openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&json=1"
    )
    if response.status_code == 200:
        return response.json().get('products', [])
    return []