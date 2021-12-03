from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_create_country_get(self):
        response = self.client.get(url_for('create_country'))
        self.assert200(response)

    def test_read_countries_get(self):
        response = self.client.get(url_for('read_countries'))
        self.assert200(response)

    def test_update_country_get(self):
        response = self.client.get(url_for('update_country', id=1))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_countries(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)

class TestCreate(TestBase):

    def test_create_country(self):
        response = self.client.post(
            url_for('create_country'),
            data={"country_name": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
class TestUpdate(TestBase):

    def test_update_country(self):
        response = self.client.post(
            url_for('update_country', id=1),
            data={"country_name": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
    # def test_visited_country(self):
    #     response = self.client.get(url_for('visited_country', id=1), follow_redirects=True)
    #     self.assertEqual(Country.query.get(1).visited, True)
    
    # def test_unvisited_country(self):
    #     response = self.client.get(url_for('unvisited_country', id=1), follow_redirects=True)
    #     self.assertEqual(Country.query.get(1).visited, False)
        

class TestDelete(TestBase):

    def test_delete_country(self):
        response = self.client.get(
            url_for('delete_country', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
