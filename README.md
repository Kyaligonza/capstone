CAPSTONE PROJECT: Casting Agency App - MyappHsbk
-----

### Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and you are creating a system to simplify and streamline your process.


### Overview

This app has two models namely Artist and Movies with attributes of name, age and gender for the artists and title, release_date and country for Movies. Once the fully functioning application is deployed you will be able to query the following through the PostgreSQL database(run locally) or the virtual database hosted on Heroku (https://myapphsbk.herokuapp.com/actors):

* GET /actors and /movies
* POST /actors and /movies and
* DELETE /actors/ and /movies/
* PATCH /actors/ and /movies/

We want myapphsbk to be a platform that will help all exec producers to best manage their resources and time. And also in setting up this application we hope you will enhance your skills in the Tech Stack outlined below covered more extensively in the Udacity FullStack Nanodegree.  Goodluck and have fun learning!

### Tech Stack

The tech stack includes:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations (locally)
* **Heroku**, **Auth0**, and **Unittest** for deployment and testing.  


### Development Setup [Focus is production env below]

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you dont have it.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=app
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)

### Production Environment
### API DOCUMENTATION

This API's base URL is https://myapphsbk.herokuapp.com/actors
### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, simple web page application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `delete:actors`
    - `delete:movies`
    - `get:actors`
    - `get:movies`
    - `patch:actors`
    - `patch:movies`
    - `post:actors`
    - `post:movies`

6. Create new roles for:
    - Casting assistant
        - can `get:actors`
        - can `get:movies`
    - Casting director
        - can `get:actors`
        - can `get:movies`
        - can `patch:actors`
        - can `patch:movies`
        - can `post:actors`
        - can `delete:actors`   
    - Eecutive producer
        - can perform all actions
7. Update `./auth/auth.py` with the new variables for Auth0_Domain and Audience.
8. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users - assign the above roles to them.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter/myapphsbk.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection. 

### AUTHENTICATION (Note this a temporay API and many of the sensitive environment variables will be removed at a later stage )
Consuming the API through CURL or POSTMAN ( `./starter/myapphsbk.postman_collection.json`) the JWT tokens are provided in the config.py file as follows:
bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZWQ2OWM1MTA2MDA2ZGUyMzNjNCIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAwODExODgwLCJleHAiOjE2MDA4OTgyODAsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.UNc_I9utPjpp-kOMANBFNTQOI92yWY-GOPkNt4lSXVMm8VdUmSXm5_24dlUpapJGKUA2glLSTWpk5qBi4ip1ZDn7Dq_2RCluzZPx7zqzL5kgse2VIUuN7z5qPx5bk_ZpuVLbVsmW1VsrZ2SUdClep7pqMtMjlfuQpC2gaz6B4rJSwOKUit6sYnkvM11osOARGpit9NxeMGaCDfwFld_uf8JOiddfSW-rDXQSHYSNa4l4qc33D4HdCqK50hKrrv5e8YP8pLDFeS6n5jDgu68311JxuQh7us3l_sN4sDpv5OZwvoDdaGAD5VvN91KfeMS6gQv041IeDAMFdd6LKpvFUg",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5YzExYzY0NzhiMDA2N2Q5MGU0MyIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAwODExMzYyLCJleHAiOjE2MDA4OTc3NjIsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.ivUg3eiI4SBFsLmhrnkWnivxKBu9QhNitG3FW2xUHJeoD6gbAszFSlRX_r1_-LXuUV3j1UZIKCOMokjjEvxxfzIgMIN6-92y4RJmJkvHjOoVgLvGTc7IJDcEzdmvNTFVZbPjwtaOzoLNdM8uxw_rSd2vhj4luaPAnLaLEnf4x83i8VLAASKqi9a5d2ri4t0rDc0y7q6vT9so2zB91qPRN1mdxOUahUo8fC9CyTqBJOG58CKzfbH5_3yQV4IBBhVV3qTM4yVFLMiICKtrDLRlpKEHqUrTd2-h-rs5NWQf6sjtXjRxekJELY5E9JGHT86sJ5i84QbQ8EVAS39damncWg",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZGMxMjA3NmE3MDA2NzhmODM4OSIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAwODExNTk5LCJleHAiOjE2MDA4OTc5OTksImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.NBC446VZgBDlqpnjphEQmKv3Ku6HZHWtpPowbTcqNR7GLEWmi1C6TT-IcsUvmu5qabMMAK5FGic_tzCy8OarnWoKBjJufuWXdlr02bFDr4g8XLGTq0BfB16Ckg8d6ab9z65icXyel4va3ZxRHIB0eInbdLhO7xkwNh9SJTb3beeyHunIRWVF2GZJEFrc4dsmflfUlRQF3OZWNit5jb2dVouJTqblkRetIidz4C8Px_uVovvauT0w6g0Y9LXqLe86__O_oJYZ3Ti7ZELhDoG3yT9rMVjUKn3K_ELdO6t2y2WtQAom5zK8_0vn8kPLYoNf0XewoFhYBwf1dE-s5vNSwQ"
}
To refresh the tokens or access through the URL then the following sign-in link and username-password accesses are available:
1. AUth0 JWT link: https://agent88.us.auth0.com/authorize?audience=stars&response_type=token&client_id=xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ&redirect_uri=https://myapphsbk.herokuapp.com/actors

2. Grant Access enter the following as required:

   casting assistant angela@gmail.com  Password Angela@2020
   casting director david@gmail.com Password David@2020
   executive producer sarah.kyaligonza@gmail.com Password Auth0@2020


### Endpoints
 
Endpoints
GET '/actors'
GET ...
POST ...
DELETE ...

GET '/actors'
- Fetches a dictionary of actors in which the keys are actors, success and the value is the corresponding string of actors and their features.
- Request Arguments: None
- Returns: An object with two keys, success and actors which contains list objects of key:value pairs represented below.
{
    "actors": [
        {
            "age": 58,
            "gender": "male",
            "id": 1,
            "name": "Tom Cruise"
        },
        {
            "age": 56,
            "gender": "male",
            "id": 2,
            "name": "Keanu Reeves"
        },
        {
            "age": 48,
            "gender": "Female",
            "id": 3,
            "name": "Jada Pinkett"
        }
    ],
    "success": true
}
GET '/movies'
- Fetches a dictionary of movies in which the keys are movies, success and the value is the corresponding string of movies and their features.
- Request Arguments: None
- Returns: An object with two keys, success and movies which contains list objects of key:value pairs represented below.
{
    "movies": [
        {
            "country": "USA",
            "id": 1,
            "release_date": "Thu, 15 May 2003 00:00:00 GMT",
            "title": "The MAtrix Reloaded"
        },
        {
            "country": "USA",
            "id": 2,
            "release_date": "Fri, 16 May 1986 00:00:00 GMT",
            "title": "Top Gun"
        },
        {
            "country": "UK",
            "id": 3,
            "release_date": "Thu, 10 Jul 2003 00:00:00 GMT",
            "title": "Love Actually"
        }
    ],
    "success": true
}

DELETE '/actors/<int:actor_id>'
- Deletes an actor using an actor id.
- Request Arguments: actor id
- Returns: An object with two keys, success and id of the actor deleted, that contains an object of key:value pairs as follows. 

{
    "delete": 13,
    "success": true
}

DELETE '/movies/<int:movie_id>'
- Deletes a movie using a movie id.
- Request Arguments: movie id
- Returns: An object with two keys, success and id of the movie deleted, that contains an object of key:value pairs as follows. 

{
    "delete": 6,
    "success": true
}

POST '/actors'

- Creates a new actor, which takes the name,age and gender attributes.
- Request Arguments: None
- Returns: An object with a two keys,success and actors with id of actor created that contains objects of key:value pairs represented below.

{
    "actors": 14,
    "success": true
}

POST '/movies'

- Creates a new movie, which takes the title,release_date and country attributes.
- Request Arguments: None
- Returns: An object with a two keys,success and movies with id of movie created that contains objects of key:value pairs represented below.

{
    "movies": 7,
    "success": true
}

PATCH '/actors/<int:actor_id>'

- Updates an actor's details whose actor_id is submitted.
- Request Arguments: actor_id
- Returns: An object with two keys, success, actor with updated details  which contains a list of key:value pairs represented below.
{
    "actor": [
        {
            "age": 75,
            "gender": "male",
            "id": 12,
            "name": "Harrison Ford"
        }
    ],
    "success": true
}

PATCH '/movies/<int:movie_id>'

- Updates and movie's details whose movie_id is submitted.
- Request Arguments: movie_id
- Returns: An object with two keys, success, movie with updated details  which contains a list of key:value pairs represented below.
{
    "movies": [
        {
            "country": "Venus",
            "id": 7,
            "release_date": "Thu, 16 Feb 1939 00:00:00 GMT",
            "title": "Gone with the wind"
        }
    ],
    "success": true
}

```
Error handling
Error messages will appear in the following format:
{
    "success":False,
    "error":404,
    "message":item not found
}
The API captures seven errors types when the requests fail:
    .400: Bad request
    .401: Unauthorised
    .403: Forbidden
    .404: Item not found
    .405: Method Not Allowed
    .422: unprocessable
    .500: Server Error

### Testing
To run the tests, run
```
python3 test_app.py
```
Expected result: 
Ran 16 tests in 6.707s

OK
