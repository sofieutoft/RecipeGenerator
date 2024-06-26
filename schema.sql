# Create table
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal TEXT NOT NULL,
    cuisine TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);
