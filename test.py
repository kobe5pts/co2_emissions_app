import unittest
from co2_emissions import co2_emissions

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the CO2 Emissions Search App', response.data)

    def test_co2_emissions_page(self):
        response = self.app.get('/co2_emissions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CO2 Emissions Search', response.data)

    def test_invalid_entity(self):
        response = self.app.post('/search_results_co2_emissions', data={'entity': 'InvalidEntity', 'year': '2020'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The entity InvalidEntity does not exist', response.data)

    def test_entity_not_provided(self):
        response = self.app.post('/search_results_co2_emissions', data={'year': '2020'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Entity not provided', response.data)

    def test_year_not_provided(self):
        response = self.app.post('/search_results_co2_emissions', data={'entity': 'China'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Year not provided', response.data)

    def test_search_results(self):
        response = self.app.post('/search_results_co2_emissions', data={'entity': 'China', 'year': '2020'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search Results', response.data)
        self.assertIn(b'China', response.data)
        self.assertIn(b'2020', response.data)

    def test_entity_not_found(self):
        response = self.app.post('/search_results_co2_emissions', data={'entity': 'InvalidEntity', 'year': '2020'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No data found for the entity InvalidEntity', response.data)

if __name__ == '__main__':
    unittest.main()
