import React from 'react';
import './Navbar.css';

const Navbar = ({ query, setQuery, searchRecipes }) => {
    return (
        <header className="app-header">
            <div className="header-content">
                <img src={`${process.env.PUBLIC_URL}/LetThemCook.png`} alt="LetThemCook Logo" className="logo" />
                <div className="search-bar">
                    <input
                        type="text"
                        placeholder="Search for a meal"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                    />
                    <button onClick={searchRecipes}>Search</button>
                </div>
            </div>
        </header>
    );
};

export default Navbar;