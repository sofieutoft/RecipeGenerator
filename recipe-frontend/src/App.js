import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [query, setQuery] = useState('');
    const [cuisine, setCuisine] = useState('');
    const [results, setResults] = useState([]);
    const [recipes, setRecipes] = useState([]);
    const [recipeDetails, setRecipeDetails] = useState(null);
    const [error, setError] = useState(null);

    const searchRecipes = async () => {
        try {
            const response = await axios.post('/api/search', { query, cuisine });
            setResults(response.data.results);
        } catch (err) {
            console.error('Error searching recipes:', err);
            setError('Failed to search recipes. Please try again.');
        }
    };

    const addRecipe = async (dish_id) => {
        try {
            const response = await axios.get(`/api/add_recipe/${dish_id}`);
            alert(response.data.message);
        } catch (err) {
            console.error('Error adding recipe:', err);
            setError('Failed to add recipe. Please try again.');
        }
    };

    const viewRecipes = async () => {
        try {
            const response = await axios.get('/api/view_recipes');
            setRecipes(response.data);
        } catch (err) {
            console.error('Error viewing recipes:', err);
            setError('Failed to view recipes. Please try again.');
        }
    };

    const viewRecipeDetails = async (dish_id) => {
        try {
            const response = await axios.get(`/api/recipe/${dish_id}`);
            setRecipeDetails(response.data);
        } catch (err) {
            console.error('Error viewing recipe details:', err);
            setError('Failed to view recipe details. Please try again.');
        }
    };

    return (
        <div>
            <h1>Search for Recipes</h1>
            <input
                type="text"
                placeholder="Query"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <input
                type="text"
                placeholder="Cuisine"
                value={cuisine}
                onChange={(e) => setCuisine(e.target.value)}
            />
            <button onClick={searchRecipes}>Search</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ul>
                {results.map((result) => (
                    <li key={result.id}>
                        {result.title} <button onClick={() => addRecipe(result.id)}>Add</button>
                    </li>
                ))}
            </ul>

            <h2>All Recipes</h2>
            <button onClick={viewRecipes}>View All Recipes</button>
            <ul>
                {recipes.map((recipe) => (
                    <li key={recipe.meal_id}>
                        {recipe.meal_name} - {recipe.cuisine}
                        <button onClick={() => viewRecipeDetails(recipe.meal_id)}>View Details</button>
                    </li>
                ))}
            </ul>

            {recipeDetails && (
                <div>
                    <h3>Recipe Details</h3>
                    <p><strong>Ingredients:</strong></p>
                    <ul>
                        {recipeDetails.ingredients.map((ingredient, index) => (
                            <li key={index}>{ingredient.name}: {ingredient.amount.us.value} {ingredient.amount.us.unit}</li>
                        ))}
                    </ul>
                    {recipeDetails.recipe_card_url && (
                        <img src={recipeDetails.recipe_card_url} alt="Recipe Card" />
                    )}
                    {recipeDetails.error_message && (
                        <p>{recipeDetails.error_message}</p>
                    )}
                </div>
            )}
        </div>
    );
}

export default App;
