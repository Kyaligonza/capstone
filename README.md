CAPSTONE PROJECT: Casting Agency App - MyappHSBK
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
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection. 

### AUTHENTICATION (Note this a temporay API and many of the sensitive environment variables will be removed at a later stage )
Consuming the API through CURL or POSTMAN ( `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`) the JWT tokens are provided in the config.py file as follows:
bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZWQ2OWM1MTA2MDA2ZGUyMzNjNCIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAwMzg0NTY5LCJleHAiOjE2MDA0NzA5NjksImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.N_EmzXAi-BB6t6zWp04yjm1cd0LKYVOnYXa0IiLsJiRjNgR-ABGhCMxdZgxeTvLFXKcd7GDNdJiRunC7KzuIIzvlKtbgbHn8wFjwNbjjvwODXfD1zZwozfai4st6IivaGaqNiSEt2jI7RMYJCamMmTlbBm9n6WXz3ZG5ibTUzSHy0gxFHhy03GLWcnzrx_5fr0FIzCy2bVa-grPf-w9dNOIpNfPLntPcLrh3XvLwJDgBTU4VltHCTGIOdFXUBRw3DJ_9EMUsBjhpmepSI9s2PEQrpOz6miobLqcG_6KvMAP2lPp88P-nks7BG1CDSEe-qrM91-ZntJRjyfM8LUry-A",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaQGNsaWVudHMiLCJhdWQiOiJzdGFycyIsImlhdCI6MTYwMDM5MDk4OCwiZXhwIjoxNjAwNDc3Mzg4LCJhenAiOiJ4Rm9HOFI3MUVFRlhtSElPS1B4R0xwZFRRQ0cyaVpWWiIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIHBvc3Q6YWN0b3JzIHBvc3Q6bW92aWVzIGRlbGV0ZTphY3RvcnMgZGVsZXRlOm1vdmllcyBwYXRjaDphY3RvcnMgcGF0Y2g6bW92aWVzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiXX0.NdONqHECV3Op63WD_9gDR9PUVmolbJ8kZ-nSG6Plum2OF7fM0obG2NVO50fSYG38zikQuTI-_W5Qs4vsIT1WH98ACG0VEe48op7X72Qia0nkYkWGY_cE8A6wPmnNb1b8vn1vFbTImwd_dOObmI3lmfcpvsoWAkAYUSSb6G09WUpNtWDI3zdv3BCF95KRmLb3BH0Uw7VFpA3MzP_K8TV5P4z7FqTE5MnHvioUYaz0rrLLSDhTHWSHl79M6opQtmg56nvJPoHu6FmVAwwYr1lo-ZeKAQnP6ylNyxwEMXRY5CgVywR2RXh3ivnfSKsLXIACwIGmelmtjO1HWp-PQSHzdw",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Indlc2FPUHp5TGNBTUtkLTlaSmlydCJ9.eyJpc3MiOiJodHRwczovL2FnZW50ODgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNTI5ZGMxMjA3NmE3MDA2NzhmODM4OSIsImF1ZCI6InN0YXJzIiwiaWF0IjoxNjAwMzg0NzAzLCJleHAiOjE2MDA0NzExMDMsImF6cCI6InhGb0c4UjcxRUVGWG1ISU9LUHhHTHBkVFFDRzJpWlZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.IpU3FrBMsnRLRO9ErMbcFx2U_GGLZQ7LwFhnQHSZcPYwk8ovxjuQXnRRDtHcAHspY0TUIkpP1HMFAMXXtSRsX5iRfQzkrb1fgdVvnkkasrbIrdHCdJlVsxbaxEcjsMuAff7XwTXrGJkI-e2s7l9Z5WqO5Gfm64Fu-yJ6_knOeTjFlQLciLcu-ORIq9dB-EQjT6ogmHCDnDvlPi6at03fHgcrEEHtrC4n6LJlyeYDDgQLtjpXxExpKSMd485_8MLTP7QAsml-krBnM_ptSOzeJ7BuYVl1mz31xpKD88wCWyFgo2qRzQZj9hfU0rMM4vfRxi8JbarOA6F2n7NXNqVg-g"
}
To refresh the tokens or access through the URL then the following sign-in link and username-password accesses are available:
1. AUth0 JWT link: https://agent88.us.auth0.com/authorize?audience=stars&response_type=token&client_id=xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ&redirect_uri=https://myapphsbk.herokuapp.com/actors

2. Grant Access enter the following as required:

   casting assistant angela@gmail.com  Password Angela@2020
   casting director david@gmail.com Password David@2020
   executive producer sarah.kyaligonza@gmail.com Password Auth0@2020


### Endpoints
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a dictionary of questions in which the keys are the categories,questions,success and total_questions; and the value is the corresponding list for categories and questions, string and int for success and total_questions respectively:
- Request Arguments: None
- Returns: An object with four keys, categories,success, total_questions and questions which contains list objects of key:value pairs represented below.
 
{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 3, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      ......
    },
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 35
}

GET '/categories/<int:category_id>/questions'
- Fetches a dictionary of questions based on categories.
- Request Arguments: category_id
- Returns: An object with three keys,success, total_questions and questions which contains a list of key:value pairs represented below.
{
  "questions": [
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 1, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 1, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 1, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 36
}

DELETE '/questions/<int:question_id>'
- Deletes a question using a question id.
- Request Arguments: question id
- Returns: An object with two keys, success and id of the question deleted, that contains an object of key:value pairs as follows. 

{
    "success":True,
    "item_deleted":24
}

POST '/questions'
C:\Users\hp>curl -X POST -H "Content-Type:application/json" -d "{  \"question\" : \"who is Frodo\",  \"answer\" : \"Baggins of course in Lord of the rings\",\"category\":4 }" http://localhost:5000/questions

- Creates a new question, which requires the question and answer text, 
  category, and difficulty score.
- Request Arguments: None
- Returns: An object with a two keys,success and total_questions that contains objects of key:value pairs represented below.

{
  "Total_questions": 36,
  "success": true
}

POST '/questions'
C:\Users\hp>curl -X POST -H "Content-Type:application/json" -d "{  \"searchTerm\":\"city\" }" http://localhost:5000/questions

- Retrieves question(s) based on a serach term, requires a string searchTerm to be provided.
- Request Arguments: None
- Returns: An object with four keys,success, categories, suggested_nb of questions and questions which contains a list of key:value pairs represented below.
{
  "categories": [
    "Science",
    "Art",
    "Geography",
    "History",
    "Entertainment",
    "Sports"
  ],
  "questions": [
    {
      "answer": "Agra",
      "category": 2,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Vancouver",
      "category": 2,
      "difficulty": 2,
      "id": 24,
      "question": "greatest city in the world"
    },
    {
      "answer": "rome",
      "category": 0,
      "difficulty": 4,
      "id": 27,
      "question": "Capital city of Italy?"
    }
  ],
  "success": true,
  "suggested_nb": 3
}

POST '/quizzes'
C:\Users\hp>curl -X POST -H "Content-Type:application/json" -d "{\"quiz_category\":"{\"id\":1,\"type\":\"Art\"}", \"previous_questions\":[]}" http://localhost:5000/quizzes

- Retrieves randomn question by category to play the quiz, requires quiz_category id and the list of previous_questions to be provided.
- Request Arguments: quiz_category id and a list of previous_questions.
- Returns: An object with three keys, success, question and previous_questions which contains a list of key:value pairs represented below.
{
  "previous_questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "question": {
    "answer": "Escher",
    "category": 2,
    "difficulty": 1,
    "id": 16,
    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
  },
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
The API captures four errors types when the requests fail:
    .400: Bad request
    .404: Item not found
    .405: Method not allowed for this end point
    .422: Something amiss try again

### Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

