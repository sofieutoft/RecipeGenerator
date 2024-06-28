import React from 'react';
import './RecipeCard.css';

const RecipeCard = ({ result, viewRecipeDetails }) => {
    return (
        <li className="result-item">
            <img src={result.image} alt={result.title} />
            <div className="result-info">
                <h2>{result.title}</h2>
                <button onClick={() => viewRecipeDetails(result.id)}>View Recipe</button>
            </div>
        </li>
    );
};

export default RecipeCard;