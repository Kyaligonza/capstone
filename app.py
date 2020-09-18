import os
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS, cross_origin
from models import setup_db, Actors, Movies
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)

    CORS(app,resources={r"/*": {"origins": "*"}})

    # @app.after_request
    # def after_request(response):
    #   response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    #   response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE')
    #   return response

    
    @app.route('/actors', methods=['GET'])
    # @cross_origin
    @requires_auth('get:actors')
    def get_actors(payload): 
        try:
            actors = Actors.query.order_by(Actors.id).all()
            actorx = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': actorx
            }), 200
        except:
            abort(500)  

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload): 
        try:
            movies = Movies.query.order_by(Movies.id).all()
            moviex = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'movies': moviex
            }), 200
        except:
            abort(500)  

    
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload,actor_id):      
        actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                "success": True,
                "delete": actor_id
            }), 200
        except BaseException:
            abort(500)
    
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload,movie_id):      
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                "success": True,
                "delete": movie_id
            }), 200
        except BaseException:
            abort(500)
    
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(payload):  
        body = request.get_json()
        try:
            req_name = body.get("name", None)
            req_age = int(body.get('age', None))
            req_gender = body.get('gender', None)
            actor = Actors(
                name=req_name,
                age=req_age,
                gender=req_gender
            )

            actor.insert()

            return jsonify({
                'success': True,
                'actors': actor.id
            }), 200
        except BaseException:
            abort(422)
    
    
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):  
        body = request.get_json()
        try:
            req_title = body.get("title", None)
            req_release = body.get("release_date", None)
            req_country = body.get("country", None)
            movie = Movies(
                title=req_title,
                release_date=req_release,
                country=req_country
            )

            movie.insert()

            return jsonify({
                'success': True,
                'movies': movie.id
            }), 200
        except BaseException:
            abort(422)
    

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload,actor_id): 

        body = request.get_json()

        try:
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            if 'name' in body:
                actor.name = body.get('name')
            if 'age' in body:
                actor.age = int(body.get('age'))
            if 'gender' in body:
                actor.gender = body.get('gender')

            actor.update()
            actor_updated = Actors.query.filter(Actors.id == actor_id).one_or_none()

            return jsonify({
                'success': True,
                'actor': [actor_updated.format()]
            }), 200

        except:
            abort(422)

    
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload,movie_id): 

        body = request.get_json()

        try:
            movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
            if movie is None:
                abort(404)

            if 'title' in body:
                movie.title = body.get('title')
            if 'release_date' in body:
                movie.release_date = body.get('release_date')
            if 'country' in body:
                movie.country = body.get('country')

            movie.update()
            movie_updated = Movies.query.filter(Movies.id == movie_id).one_or_none()

            return jsonify({
                'success': True,
                'movies': [movie_updated.format()]
            }), 200

        except:
            abort(422)

    @app.route('/coolkids')
    def be_cool():
        return "This is our time, the time is now...FSND graduate #excited!!!!"



    # Error Handling
    '''
    Error handling for unprocessable entity, resource not found, server error and auth_errors
    '''


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Server Error"
        }), 500


    '''
    Error handler for AuthError

    '''

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code


    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": 'Method Not Allowed'
        }), 405


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request'
        }), 400


    @app.errorhandler(401)
    def unauthorised(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unauthorised'
        }), 401


    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": 'Forbidden'
        }), 403
        

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
    # app.run(host='127.0.0.1', port=5000, debug=True)