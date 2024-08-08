import requests
import json


class Breed:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


def validate_breed(breed_name):
    url = "https://api.thecatapi.com/v1/breeds"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"client: error making HTTP request: {e}")
        return False

    try:
        breeds = response.json()
    except json.JSONDecodeError as e:
        print(f"client: could not decode JSON: {e}")
        return False

    # A set to store breed names for efficient lookup
    all_breeds = {breed["name"] for breed in breeds}

    return breed_name in all_breeds
