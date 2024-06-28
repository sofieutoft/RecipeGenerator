import React, { useState } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar/Navbar';
import RecipeCard from './components/RecipeCard/RecipeCard';
import RecipeDetails from './components/RecipeDetails/RecipeDetails';
import './App.css';

function App() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [recipeDetails, setRecipeDetails] = useState(null);
    const [error, setError] = useState(null);

    const searchRecipes = async () => {
        try {
            const response = await axios.get(`https://api.spoonacular.com/recipes/complexSearch?query=${query}&apiKey=${process.env.REACT_APP_API_KEY}`);
            setResults(response.data.results);
            setRecipeDetails(null); 
            setError(null);
        } catch (err) {
            console.error('Error searching recipes:', err);
            setError('Failed to search recipes. Please try again.');
        }
    };

    const viewRecipeDetails = async (id) => {
        try {
            const response = await axios.get(`https://api.spoonacular.com/recipes/${id}/information?apiKey=${process.env.REACT_APP_API_KEY}`);
            setRecipeDetails(response.data);
            setError(null);
        } catch (err) {
            console.error('Error viewing recipe details:', err);
            setError('Failed to view recipe details. Please try again.');
        }
    };

    return (
        <div className="app-container">
            <Navbar query={query} setQuery={setQuery} searchRecipes={searchRecipes} />
            <div className="joke">
                <p>Wanna hear a joke about pizza? Never mind, it’s too cheesy.</p>
            </div>
            {error && <p className="error-message">{error}</p>}
            <div className="content-container">
                <div className="results-container">
                    <ul className="results-list">
                        {results.map((result) => (
                            <RecipeCard key={result.id} result={result} viewRecipeDetails={viewRecipeDetails} />
                        ))}
                    </ul>
                </div>
                {recipeDetails && <RecipeDetails recipeDetails={recipeDetails} />}
            </div>
        </div>
    );
}

export default App;