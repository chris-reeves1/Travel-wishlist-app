from flask import url_for
from flask_testing import TestCase
from application import app
from application.routes import backend_host
import requests_mock

test_country = {
                "id": 1,
                "country_name": "test country",
                "visited": False
            }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            all_countries = { "country": [test_country] }
            m.get(f"http://{backend_host}/read/allCountries", json=all_tasks)
            response = self.client.get(url_for('home'))
            self.assert200(response)
    
    def test_create_country_get(self):
        response = self.client.get(url_for('create_country'))
        self.assert200(response)

    def test_update_country_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/country/1", json=test_country)
            response = self.client.get(url_for('update_country', id=1))
            self.assert200(response)

class TestRead(TestBase):

    def test_read_home_countries(self):
        with requests_mock.Mocker() as m:
            all_countries = { "country": [test_country] }
            m.get(f"http://{backend_host}/read/allCountries", json=all_tasks)
            response = self.client.get(url_for('home'))
            self.assertIn(b"Test the frontend", response.data)

class TestCreate(TestBase):

    def test_create_country(self):
        with requests_mock.Mocker() as m:
            all_countries = { "country": 
                [
                    test_country,
                    {
                        "id": 2,
                        "country_name": "Testing create functionality",
                        "visited": False
                    }
                ] 
            }
            m.post(f"http://{backend_host}/create/country", text="Test response")
            m.get(f"http://{backend_host}/read/allCountries", json=all_tasks)
            response = self.client.post(
                url_for('create_country'),
                json={"country_name": "Testing create functionality"},
                follow_redirects=True
            )
            self.assertIn(b"Testing create functionality", response.data)
    
class TestUpdate(TestBase):

    def test_update_country(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/read/country/1", json=test_task)
            m.put(f"http://{backend_host}/update/country/1", text="Test response")
            test_country["country_name"] = "Testing update functionality"
            m.get(f"http://{backend_host}/read/allCountries", json={ "country": [test_country] })
            response = self.client.post(
                url_for('update_country', id=1),
                data={"country_name": "Testing update functionality"},
                follow_redirects=True
            )
            self.assertIn(b"Testing update functionality", response.data)
    
    def test_visited_country(self):
        with requests_mock.Mocker() as m:
            m.put(f"http://{backend_host}/visited/country/1")
            test_country["visited"] = True
            m.get(f"http://{backend_host}/read/allCountries", json={ "country": [test_country] })
            response = self.client.get(url_for('visited_country', id=1), follow_redirects=True)
            self.assert200(response)
    
    def test_unvisited_country(self):
        with requests_mock.Mocker() as m:
            m.put(f"http://{backend_host}/unvisited/country/1")
            test_country["visited"] = False
            m.get(f"http://{backend_host}/read/allCountries", json={ "country": [test_country] })
            response = self.client.get(url_for('unvisited_country', id=1), follow_redirects=True)
            self.assert200(response)
        

class TestDelete(TestBase):

    def test_delete_country(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend_host}/delete/country/1")
            m.get(f"http://{backend_host}/read/allCountries", json={ "country": [] })
            response = self.client.get(
                url_for('delete_country', id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"Test the frontend", response.data)