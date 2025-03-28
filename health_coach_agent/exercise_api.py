from diskcache import Cache
import requests

BASE_URL = "https://exercisedb-api.vercel.app/api/exercises"
cache = Cache('./cache_dir')

# Function to get exercises by target muscle with caching
def get_exercises_by_target(target):
    if target in cache:
        return cache[target]
    
    response = requests.get(f"{BASE_URL}/target/{target}")
    if response.status_code == 200:
        result = response.json()
        cache[target] = result     # Store result in cache
        return result
    return []                       # Return empty list if request fails


# Function to get exercises by equipment
def get_exercises_by_equipment(equipment):
    response = requests.get(f"{BASE_URL}/equipment/{equipment}")
    if response.status_code == 200:
        return response.json()
    return []                       # Return empty list if request fails