import React from 'react';
import './RecipeDetails.css';

const RecipeDetails = ({ recipeDetails }) => {
    return (
        <div className="recipe-details">
            <h2>{recipeDetails.title}</h2>
            <img src={recipeDetails.image} alt={recipeDetails.title} />
            <div className="tags">
                <span className="tag">Top-20</span>
                <span className="tag">Easy</span>
                <span className="tag">Popular</span>
            </div>
            <div className="recipe-info">
                <p className="summary"><strong>Need a gluten-free and dairy-free side dish?</strong> Refried Beans with Chorizo could be an excellent recipe to try.</p>
                <p className="details">
                    <span><strong>Cost:</strong> 55 cents per serving</span>
                    <span><strong>Nutrition:</strong> 13g protein, 4g fat, 213 calories per serving</span>
                    <span><strong>Servings:</strong> 6</span>
                    <span><strong>Prep Time:</strong> 45 minutes</span>
                    <span><strong>Rating:</strong> Liked by 1 foodies and cooks</span>
                    <span><strong>Source:</strong> Foodista</span>
                    <span><strong>Ingredients:</strong> Pepper, cilantro, chorizo, and more</span>
                </p>
                <p className="score"><strong>Spoonacular Score:</strong> 87% - This dish is super!</p>
                <p className="similar-recipes"><strong>Similar Recipes:</strong> Chorizo Refried Beans, Huevos Rancheros with Chorizo Refried Beans, and Sopes with Chorizo Refried Beans and a Tangy Slaw.</p>
            </div>
            <div className="taste-profile">
                <strong>Taste:</strong>
                <div className="taste">
                    <span>Bitter</span>
                    <span>Sweet</span>
                    <span>Sour</span>
                    <span>Salty</span>
                    <span>Umami</span>
                </div>
            </div>
            <h3>Recipe</h3>
            <ul className="ingredients-list">
                {recipeDetails.extendedIngredients.map((ingredient, index) => (
                    <li key={index}>{ingredient.original}</li>
                ))}
            </ul>
            <h3>Instructions</h3>
            <p dangerouslySetInnerHTML={{ __html: recipeDetails.instructions }}></p>
        </div>
    );
};

export default RecipeDetails;