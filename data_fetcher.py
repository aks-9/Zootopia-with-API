import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "T5lXtQQeK2SiSNcvvZWNIKs1oIhYa5RNv4EEZozI"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.

    Returns:
    A list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {...},
      'locations': [...],
      'characteristics': {...}
    }
    """
    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "name": animal_name
    }

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()

    return response.json()
