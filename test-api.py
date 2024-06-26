import os
from pprint import pprint
import requests


def print_available_meals(data):
    for result in data['results']:
        print(result['id'], '---->', result['title'])


def print_ingredients(dish_id):
    print('\nINGREDIENTS: \n')
    ingredients_url = f'https://api.spoonacular.com/recipes/{dish_id}/ingredientWidget.json'
    ingredients = requests.get(ingredients_url, params={'apiKey': api_key})
    ingredients = ingredients.json()
    for ingredient in ingredients['ingredients']:
        amount = ingredient['amount']['us']['value']
        unit = ingredient['amount']['us']['unit']
        name = ingredient['name']
        print(f"- {amount} {unit} of {name}")


def print_instructions(dish_id):
    print('\nINSTRUCTIONS: \n')
    dish_url = f'https://api.spoonacular.com/recipes/{dish_id}/information'
    instruction_response = requests.get(dish_url, params={'apiKey': api_key})
    instructions = instruction_response.json()
    print(instructions['instructions'])


if __name__ == '__main__':
    api_key = os.getenv('API_KEY')
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    query = input("Name of dish: ")
    cuisine = input("Enter cuisine: ")
    parameters = {
        'apiKey': api_key,
        'query': query,
        'cuisine': cuisine
    }
    response = requests.get(url, params=parameters)
    data = response.json()

    if data['totalResults'] >= 1:
        print("!----- Available meals -----!")
        print("Please select the id of the meal whose recipe you'd like: ")
        print_available_meals(data)
        dish_id = input('Please enter dish id: ')
        print_ingredients(dish_id)
        print_instructions(dish_id)
    else:
        print(f'No dish {query} found under {cuisine} cuisine 😭')
