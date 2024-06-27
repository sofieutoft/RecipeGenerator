# Create table
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_name TEXT NOT NULL,
    meal_id INTEGER NOT NULL,
    cuisine TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);
