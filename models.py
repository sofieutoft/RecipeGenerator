from flask_sqlalchemy import SQLAlchemy

# Implement the database
db = SQLAlchemy()

# Create a class for each table in the database
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String(50), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
