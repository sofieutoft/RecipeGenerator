from flask import request, render_template, jsonify
from app import app, db
from app.models import Recipe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recipes', methods = ['POST'])
def get_recipes():
    data = request.json
    ingredients = data.get('ingredients')
    cuisine = data.get('cuisine')

    recipes = Recipe.query.filter_by(cuisine=cuisine).all()
    matching_recipes = [recipe for recipe in recipes if set(ingredients).issubset(set(recipe.ingredients.splt(',')))]

    return jsonify([recipe.name for recipe in matching_recipes])

@app.route('/api/recipe/<int:recipe_id>', mehotds=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify({
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions
    })