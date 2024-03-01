import unittest
from flask import Flask
from co2_emissions import app

class FlaskAppTests(unittest.TestCase):

    #Set up the test client before each test case.
    def setUp(self):
        self.app = app.test_client()

    #Test the index route to ensure it returns the correct response.
    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Global CO2 Emissions Data App', response.data)

    #Test the CO2 emissions page route to ensure it returns the correct response.
    def test_co2_emissions_page(self):
        response = self.app.get('/co2_emissions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search CO2 Emissions by Country and Year', response.data)

    #Test the search results with valid input data.
    def test_search_results_with_valid_input(self):
        data = {'entity': 'Country', 'year': '2020'}
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Country Entry', response.data)

    #Test the search results with invalid entity.
    def test_search_results_with_invalid_entity(self):
        data = {'entity': 'InvalidEntity', 'year': '2020'}
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Country Entry', response.data)

    #Test the search results with missing entity field.
    def test_search_results_with_missing_entity(self):
        data = {}  # Missing 'entity' and 'year' fields
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error: Country Not Provided', response.data)

    #Test the search results with missing year field.
    def test_search_results_with_missing_year(self):
        data = {'entity': 'Country'}  # Missing 'year' field
        response = self.app.post('/search_results_co2_emissions', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Country Entry', response.data)

if __name__ == '__main__':
    unittest.main()
