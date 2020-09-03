from sqlalchemy import Column, String,Integer,Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

# database_path = os.environ['DATABASE_URL']
database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "mycapstone"
    database_path = "postgres://{}/{}".format('postgres:postgres@localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Actor
Have name, age and gender
'''
class Actors(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)

'''
Movie
Have title and release date
'''
class Movies(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  country = Column(String)
  release_date = Column(Date)