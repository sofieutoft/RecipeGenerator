import unittest
from unittest.mock import patch
from flask import template_rendered
from contextlib import contextmanager
import app

# Helper function to capture templates rendered during tests
@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

class TestFlaskApp(unittest.TestCase):
    # Setup and teardown for each test
    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.app.test_client()
        with app.app.app_context():
            app.db.create_all()

    def tearDown(self):
        with app.app.app_context():
            app.db.session.remove()
            app.db.drop_all()

    # Test the search_recipes endpoint for GET request
    @patch('app.get_available_meals')
    def test_search_recipes_get(self, mock_get_available_meals):
        mock_get_available_meals.return_value = {'totalResults': 0}
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'search_form.html', response.data)

    # Test the search_recipes endpoint for POST request
    @patch('app.get_available_meals')
    def test_search_recipes_post(self, mock_get_available_meals):
        mock_get_available_meals.return_value = {'totalResults': 1, 'results': [{'id': 123, 'title': 'Chicken Soup'}]}
        with captured_templates(app.app) as templates:
            response = self.client.post('/', data={'query': 'chicken', 'cuisine': 'American'})
            self.assertEqual(response.status_code, 200)
            template, context = templates[0]
            self.assertEqual(template.name, 'search_results.html')
            self.assertEqual(len(context['results']), 1)
            self.assertEqual(context['results'][0]['title'], 'Chicken Soup')

    # Test add_recipe endpoint
    @patch('app.requests.get')
    @patch('app.Recipe.query')
    def test_add_recipe(self, mock_query, mock_get):
        mock_query.filter_by.return_value.first.return_value = None  # No existing recipe
        mock_get.return_value.json.return_value = {'title': 'New Recipe', 'cuisines': ['Italian']}
        response = self.client.get('/add_recipe/123')
        self.assertIn(b'Added New Recipe to your recipes database.', response.data)

    # Test view_recipes endpoint
    def test_view_recipes(self):
        with captured_templates(app.app) as templates:
            response = self.client.get('/view_recipes')
            self.assertEqual(response.status_code, 200)
            template, context = templates[0]
            self.assertEqual(template.name, 'view_recipes.html')
            self.assertIsInstance(context['recipes'], list)  # Ensure it passes an iterable to the template


if __name__ == '__main__':
    unittest.main()
