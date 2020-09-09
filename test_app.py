import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import date

from app import create_app
from models import setup_db, Actors, Movies


class MyapphsbkTestCase(unittest.TestCase):
    """This class represents the myapphsbk test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "mycapstone"
        self.database_path = "postgres://{}/{}".format('postgres:postgres@localhost:5432', self.database_name)
        
        setup_db(self.app, self.database_path)
        # self.assistant_token = os.environ.get('assistant_token')
        # self.direct_token = os.environ.get('direct_token')
        # self.producer_token = os.environ.get('producer_token')
        
        self.assistant_auth_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZWQ2OWM1MTA2MDA2ZGUyMzNjNCIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNTk5NjgyMzg0LCJleHAiOjE1OTk2ODk1ODQsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.kUWOw5SJYqLNaGhDJX8memjnAjzLcw9fO0HyvsRR5JQAwGh6ieXsvxDiGouJb_NMc-iILP7h7s-WfjUb-A6YlfpqlwCF_QjfZ2FeKwvZcKAXatB_zPWR-MPNGiAh__bR5Mc9cWUsTalYCq19qJF8TmziXKKbU4h_r9BCrOxkRZ98Zvc6fx3jRp_5MHKF-4C-YNhf7oM87WRNHozh-BiJ9vnqK4mxhGmL55tpdYhIkyyXF3HG93Et4t75HZzzzkESJ9Da02JdUbnmoMCUHKXTUtzd7Roabw-aZHLbt-a7DXL5q37U5T6bZ8sQBP2kJK_5SMemSUX5uLV_lED5VaWGxg'}
        # self.assistant_auth_header = {'Authorization': 'Bearer {}'.format(self.assistant_token)}
        # self.director_auth_header = {'Authorization': 'Bearer {}'.format(self.direct_token)}
        self.director_auth_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZGMxMjA3NmE3MDA2NzhmODM4OSIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNTk5NjgzMzk4LCJleHAiOjE1OTk2OTA1OTgsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.KYyuuDoO0gXDd6FPOCQ9Kl4aR4TpyrB5ZRN6r4qfkUC7YTBH_KDTakNVcEduPfk6oBCHA_qpASMmQtxjtOOJcA3uS0RX8oE_jDVmMmdG2BPHNHS0UJms0MRcIGQ2yobnQY8JAm0NXA9DGt-k3BuLHY6MWn6K0x5gQmJ-KB4G_EjzJrXjJZTjF2645cDo5EmvKdQbO9K1UHZhzwKUzq8D2gt8WvE9VZhjDejP0GvKWztuffmHJF1I6y-yLfJqGqsFL501tCyDjM8Ts8qf-yXdKRrI65PQxBB_pf4gm8Ub9jNELWgErjvYEpoAy0H_OiAmOhN5cFsaaj-0JNiaQabCug'}
        # self.producer_auth_header = {'Authorization': 'Bearer {}'.format(self.producer_token)}
        self.producer_auth_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5YzExYzY0NzhiMDA2N2Q5MGU0MyIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNTk5NjgwNzM1LCJleHAiOjE1OTk2ODc5MzUsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.NXdTilWwmBqQL3ThDk2uctBqgO7Tl-k3KUgx5oZhpDAM3uP5kIRv1Ttts9uoBBvTj5k-VKCnTDXvcpNmr8CPa4I89JNtAbqRxxvxgIE6opifBNAWiO8ovV3tS2X70NQV7Gz8XfjuZtCwoLaCKXeLVHKjPWINsdb7ejjJhBYlt_VE_BRsy0m9MFmgHsWimxtcvMb6jhFZ6Af6eYg2njcc4V4f3ACizo6d7SnOYqWSqZblMmTIsVPLXLTAxc0DZWaH-4oZVfRHae3cU4plQOLOMWDYs9AefvrZGuKvkDgJqz8ePZi_uqxvTbzdh653aT4gy81d2ksi3dbbKR0aaDlGkQ'}
        
        self.new_actor= {
            'name': 'Ben Afleck',
            'age': 48,
            'gender': 'male'
        }
        
        self.new_actor_fail = {
            'name': 'Banji',
            'age': 'really old',
            'gender': 'male'
        }

        self.new_movie= {
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
            'age':'i dont know'
        }

        self.update_movie = {
            'country': 'UK'
        }

        self.update_movie_fail = {
            'country':24
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
    Write at least one test for each test for successful operation and for expected errors.
    """
    #GET Actors  success and failure
    def test_get_actors(self):
        res = self.client().get('/actors', headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_404_sent_requesting_unique_actor(self):
        res = self.client().get('/actors/1',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_movies(self):
        res = self.client().get('/movies', headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        # self.assertTrue(data['number_categories'])
        # self.assertTrue(len(data['categories']))

    def test_404_sent_requesting_unique_movie(self):
        res = self.client().get('/movies/1',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    # def test_get_paginated_questions(self):
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(len(data['questions']))
    
    # def test_404_sent_requesting_beyond_valid_page(self):
    #     res = self.client().get('/questions?page=888')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'item not found')
    
    # def test_405_sent_requesting_unique_question(self):
    #     res = self.client().get('/questions/12')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Method is not allowed for this endpoint')
        
    @unittest.skip("need a new actor_id otherwise will fail")
    def test_delete_actor(self):
        res = self.client().delete('/actors/2',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 2)

    
    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    @unittest.skip("need a new movie_id otherwise will fail")
    def test_delete_movie(self):
        res = self.client().delete('/movies/8',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 8)

    
    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    @unittest.skip("need a new actor_id otherwise will fail")    
    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor ,headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)  
        self.assertEqual(data['actors'], 7)


    def test_422_if_actor_creation_fails(self):
        res = self.client().post('/actors', json=self.new_actor_fail ,headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
    
    @unittest.skip("need a new movie_id otherwise will fail")    
    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie ,headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)  
        self.assertEqual(data['movies'], 9)


    def test_422_if_movie_creation_fails(self):
        res = self.client().post('/movies', json=self.new_movie_fail ,headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
    

    def test_update_actor_exist(self):
        res = self.client().patch('/actors/6',json=self.update_actor ,headers = self.producer_auth_header )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_update_actor_nonexistant(self):
        res = self.client().patch('/actors/1000' ,headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    

    def test_update_movie_exist(self):
        res = self.client().patch('/movies/5',json=self.update_movie ,headers = self.producer_auth_header )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_update_movie_nonexistant(self):
        res = self.client().patch('/movies/1000',headers = self.producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    '''RBAC test of atleast two tests for each role. Test for Executive producer
    already done above. Below we look at the RBAC tests for casting_assitant and casting_director '''

    def test_get_actors(self):
        res = self.client().get('/actors', headers = self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_delete_actor(self):
        res = self.client().delete('/actors/2',headers = self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie ,headers = self.assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)  
        self.assertEqual(data['message'], 'Permission not found.')

    # Csting Director

    def test_get_actors(self):
        res = self.client().get('/actors', headers = self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    
    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor ,headers = self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)  
        self.assertTrue(data['actors'])

    def test_update_movie_exist(self):
        res = self.client().patch('/movies/5',json=self.update_movie ,headers = self.director_auth_header )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    
    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie ,headers = self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)  
        self.assertEqual(data['message'], 'Permission not found.')

    def test_delete_movie(self):
        res = self.client().delete('/movies/9',headers = self.director_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)  
        self.assertEqual(data['message'], 'Permission not found.')






    # def test_get_question_for_quiz(self):
    #     res = self.client().post('/quizzes', json=self.quiz_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(len(data['previous_questions']),1)

    # def test_get_question_for_quiz_fail(self):
    #     res = self.client().post('/quizzes', json=self.quiz_question_fail)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)

    # def test_get_paginated_questions_by_category(self):
    #     res = self.client().get('/categories/2/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(len(data['questions']))

    # def test_422_get_paginated_questions_by_category_out_of_bound(self):
    #     res = self.client().get('/categories/8/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()