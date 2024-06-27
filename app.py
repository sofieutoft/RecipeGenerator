import os
import requests
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spoonacular_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

api_key = os.getenv('API_KEY')

def get_available_meals(query, cuisine):
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    parameters = {
        'apiKey': api_key,
        'query': query,
        'cuisine': cuisine
    }
    response = requests.get(url, params=parameters)
    return response.json()

def get_ingredients(dish_id):
    ingredients_url = f'https://api.spoonacular.com/recipes/{dish_id}/ingredientWidget.json'
    ingredients = requests.get(ingredients_url, params={'apiKey': api_key})
    return ingredients.json()

def get_recipe_card(dish_id):
    recipe_card_url = f'https://api.spoonacular.com/recipes/{dish_id}/card'
    recipe_card = requests.get(recipe_card_url, params={'apiKey': api_key})
    return recipe_card.json()

@app.route('/', methods=['GET', 'POST'])
def search_recipes():
    if request.method == 'POST':
        query = request.form.get('query')
        cuisine = request.form.get('cuisine')
        data = get_available_meals(query, cuisine)
        
        if data['totalResults'] >= 1:
            return render_template('search_results.html', results=data['results'])
        else:
            return f'No dish {query} found under {cuisine} cuisine 😭'
    
    return render_template('search_form.html')

@app.route('/add_recipe/<int:dish_id>')
def add_recipe(dish_id):
    existing_recipe = Recipe.query.filter_by(spoonacular_id=dish_id).first()
    if existing_recipe:
        return "This recipe is already in your database."
    
    url = f'https://api.spoonacular.com/recipes/{dish_id}/information'
    response = requests.get(url, params={'apiKey': api_key})
    dish_info = response.json()
    
    new_recipe = Recipe(spoonacular_id=dish_id, title=dish_info['title'])
    db.session.add(new_recipe)
    db.session.commit()
    
    return f"Added {dish_info['title']} to your recipes database."

@app.route('/view_recipes')
def view_recipes():
    recipes = Recipe.query.all()
    return render_template('view_recipes.html', recipes=recipes)

@app.route('/recipe/<int:dish_id>')
def view_recipe(dish_id):
    ingredients = get_ingredients(dish_id)
    recipe_card = get_recipe_card(dish_id)
    
    recipe_card_url = None
    error_message = None
    
    if 'url' in recipe_card:
        recipe_card_url = recipe_card['url']
    elif 'status' in recipe_card and recipe_card['status'] == 'failure':
        error_message = recipe_card.get('message', 'An error occurred while fetching the recipe card.')
    
    return render_template('recipe_details.html', 
                           ingredients=ingredients['ingredients'], 
                           recipe_card_url=recipe_card_url,
                           error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)