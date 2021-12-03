from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Country

test_country = {
                "id": 1,
                "country_name": "Run unit tests",
                "visited": False
            }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Country(country_name="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_countries(self):
        response = self.client.get(url_for('read_countries'))
        all_countries = { "country": [test_country] }
        self.assertEquals(all_countries, response.json)
    
    def test_read_country(self):
        response = self.client.get(url_for('read_country', id=1))
        self.assertEquals(test_country, response.json)

class TestCreate(TestBase):

    def test_create_country(self):
        response = self.client.post(
            url_for('create_country'),
            json={"country_name": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertEquals(b"Added country with country_name: Testing create functionality", response.data)
        self.assertEquals(Country.query.get(2).description, "Testing create functionality")
    
class TestUpdate(TestBase):

    def test_update_country(self):
        response = self.client.put(
            url_for('update_country', id=1),
            json={"country_name": "Testing update functionality"}
        )
        self.assertEquals(b"Updated country (ID: 1) with country_name: Testing update functionality", response.data)
        self.assertEquals(Country.query.get(1).country_name, "Testing update functionality")
    
    def test_visited_country(self):
        response = self.client.put(url_for('visited_country', id=1), follow_redirects=True)
        self.assertEquals(b"Country with ID: 1 set to visited = True", response.data)
        self.assertEquals(Country.query.get(1).visited, True)
    
    def test_unvisited_country(self):
        response = self.client.put(url_for('unvisited_country', id=1), follow_redirects=True)
        self.assertEquals(b"Country with ID: 1 set to visited = False", response.data)
        self.assertEquals(Country.query.get(1).visited, False)
        

class TestDelete(TestBase):

    def test_delete_country(self):
        response = self.client.delete(url_for('delete_country', id=1))
        self.assertEquals(b"Deleted country with ID: 1", response.data)
        self.assertIsNone(Country.query.get(1))