import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import date

from app import create_app
from models import setup_db, Actors, Movies
from config import bearer_tokens


class MyapphsbkTestCase(unittest.TestCase):
    """This class represents the myapphsbk test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "mycapstone"
        self.database_path = "postgres://{}/{}".format(
            'postgres:postgres@localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        self.producer_auth_header = {'Authorization': '{}'.format(
            bearer_tokens['executive_producer'])}
        self.director_auth_header = {
            'Authorization': '{}'.format(bearer_tokens['casting_director'])}
        self.assistant_auth_header = {
            'Authorization': '{}'.format(bearer_tokens['casting_assistant'])}

        self.new_actor = {
            'name': 'Ben Afleck',
            'age': 48,
            'gender': 'male'
        }

        self.new_actor_fail = {
            'name': 'Banji',
            'age': 'really old',
            'gender': 'male'
        }

        self.new_movie = {
            'title': 'Apocalypse the END',
            'release_date': '2020-09-24',
            'country': 'Global'
        }

        self.new_movie_fail = {
            'title': 'Apocalypse the END',
            'release_date': 'hopefully never',
            'country': 'Global'
        }

        self.update_actor = {
            'age': 45
        }

        self.update_actor_fail = {
            'age': 'i dont know'
        }

        self.update_movie = {
            'country': 'UK'
        }

        self.update_movie_fail = {
            'country': 24
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    """
    TODO
    Write at least one test for each test for successful
    operation and for expected errors.
    """
    # GET Actors  success and failure

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_404_sent_requesting_unique_actor(self):
        res = self.client().get('/actors/1', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_404_sent_requesting_unique_movie(self):
        res = self.client().get('/movies/1', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    """ Delete tests for actors and movies using executive producer RBAC """

    @unittest.skip("need a new actor_id otherwise will fail")
    def test_delete_actor(self):
        res = self.client().delete('/actors/11', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 11)

    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    @unittest.skip("need a new movie_id otherwise will fail")
    def test_delete_movie(self):
        res = self.client().delete('/movies/11', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 11)

    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    """Post tests for actors and movies """

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_422_if_actor_creation_fails(self):
        res = self.client().post('/actors', json=self.new_actor_fail,
                                 headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_422_if_movie_creation_fails(self):
        res = self.client().post('/movies', json=self.new_movie_fail,
                                 headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    """"Patch tests """

    def test_update_actor_exist(self):
        res = self.client().patch('/actors/6', json=self.update_actor,
                                  headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_update_actor_nonexistant(self):
        res = self.client().patch('/actors/1000', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_update_movie_exist(self):
        res = self.client().patch('/movies/5', json=self.update_movie,
                                  headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_update_movie_nonexistant(self):
        res = self.client().patch('/movies/1000', headers=self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''RBAC test of atleast two tests for each role.
    Test for Executive producer
    already done above. Below we look at the RBAC tests for
    casting_assitant and casting_director '''

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_delete_actor(self):
        res = self.client().delete('/actors/13', headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    # Casting Director permissions check

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_update_movie_exist(self):
        res = self.client().patch('/movies/5', json=self.update_movie,
                                  headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    def test_delete_movie(self):
        res = self.client().delete('/movies/9', headers=self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
