import os
from flask import Flask, request, jsonify, abort
import json
# from models import setup_db
from flask_cors import CORS
from models import setup_db, Actors, Movies

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/actors')
    def get_actors():
        try:
            actors = Actors.query.all()
            # actorsx = [item.format() for item in actors]

            return jsonify({
                'success': True,
                # 'actors': actorsx
            }), 200
        except:
            abort(500)  # server error

    @app.route('/movies')
    def get_movies():
        try:
            movies = Movies.query.all()
            # drinks = [drink.short() for drink in drink_short]

            return jsonify({
                'success': True,
                'movies': movies
            }), 200
        except:
            abort(500)  # server error
    
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    # @requires_auth('delete:drinks')
    def delete_actors(actor_id):      #def delete_actors(payload, drink_id)
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
    # @requires_auth('delete:drinks')
    def delete_movies(movie_id):      #def delete_actors(payload, drink_id)
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
    # @requires_auth('post:drinks')
    def post_actors():  #post_actors(payload)
        body = request.get_json()
        try:
            req_name = body.get("name", None)
            req_age = body.get('age', None)
            req_gender = body.get('gender', None)
            actor = Actors(
                name=req_name,
                age=req_age,
                gender=req_gender
            )

            actor.insert()

            return jsonify({
                'success': True,
                'actors': actor
            }), 200
        except BaseException:
            abort(422)
    
    
    @app.route('/movies', methods=['POST'])
    # @requires_auth('post:drinks')
    def post_movies():  #post_actors(payload)
        body = request.get_json()
        try:
            req_title = body.get("title", None)
            req_release = body.get("release_date", None)
            req_country = body.get("country", None)
            movie = Actors(
                title=req_title,
                release_date=req_release,
                country=req_country
            )

            movie.insert()

            return jsonify({
                'success': True,
                'movies': movie
            }), 200
        except BaseException:
            abort(422)
    

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    # @requires_auth('patch:drinks')
    def update_actor(actor_id): #update_drink(payload, drink_id

        body = request.get_json()

        try:
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
            if actor is None:
                abort(404)

            if 'name' in body:
                actor.name = body.get('name')
            if 'age' in body:
                actor.age = body.get('age')
            if 'gender' in body:
                actor.age = body.get('gender')

            actor.update()
            actor_updated = Actors.query.filter(Actors.id == actor_id).one_or_none()

            return jsonify({
                'success': True,
                'actor': actor_updated
            }), 200

        except:
            abort(422)

    
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    # @requires_auth('patch:drinks')
    def update_movie(movie_id): #update_drink(payload, drink_id

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
            # movie_updated = Movies.query.filter(Movies.id == movie_id).one_or_none()

            return jsonify({
                'success': True,
                'drinks': "testing"
            }), 200

        except:
            abort(422)

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()