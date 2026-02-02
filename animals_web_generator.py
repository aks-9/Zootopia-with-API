import json
import requests

def fetch_animals(query):
    """Fetch animals data from API Ninjas."""
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        "X-Api-Key": "T5lXtQQeK2SiSNcvvZWNIKs1oIhYa5RNv4EEZozI"
    }
    params = {
        "name": query
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def serialize_animal(animal_obj):
    """Serialize a single animal into an HTML <li> card."""
    output = '<li class="cards__item">\n'

    # Card title
    if 'name' in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    # Card text
    output += '  <p class="card__text">\n'

    # Diet
    diet = animal_obj.get('characteristics', {}).get('diet')
    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    # First location
    locations = animal_obj.get('locations', [])
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Type
    animal_type = animal_obj.get('characteristics', {}).get('type')
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_html(data):
    """Generate the full HTML string for all animals."""
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output

def generate_not_found_html(animal_name):
    return f'''
    <h2 style="text-align:center; color: #b00020;">
        The animal "{animal_name}" doesn't exist.
    </h2>
    '''


def main():
    animal_name = input("Enter a name of an animal: ")

    animals_data = fetch_animals(animal_name)

    with open('animals_template.html', 'r') as template_file:
        html_template = template_file.read()

    # Handle "animal not found"
    if not animals_data:
        animals_info = generate_not_found_html(animal_name)
    else:
        animals_info = generate_animals_html(animals_data)

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open('animals.html', 'w') as output_file:
        output_file.write(final_html)

    print("Website was successfully generated to the file animals.html.")



if __name__ == "__main__":
    main()
