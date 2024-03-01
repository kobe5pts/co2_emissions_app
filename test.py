import unittest
from flask import Flask
from co2_emissions import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Global CO2 Emissions Data App', response.data)

    def test_co2_emissions_page(self):
        response = self.app.get('/co2_emissions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search CO2 Emissions by Country and Year', response.data)

    def test_search_results_with_valid_input(self):
        data = {'entity': 'Country', 'year': '2020'}
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Country Entry', response.data)

    def test_search_results_with_invalid_entity(self):
        data = {'entity': 'InvalidEntity', 'year': '2020'}
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Country Entry', response.data)

    def test_search_results_with_missing_entity(self):
        data = {}  # Missing 'entity' and 'year' fields
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error: Country Not Provided', response.data)

    def test_search_results_with_missing_year(self):
        data = {'entity': 'Country'}  # Missing 'year' field
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Country Entry', response.data)

if __name__ == '__main__':
    unittest.main()
