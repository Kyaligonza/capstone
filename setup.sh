

# database_path = os.environ.get('DATABASE_URL')
# if not database_path:
#     database_name = "mycapstone"
#     database_path = "postgres://{}/{}".format('localhost:5432', database_name)

export DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/mycapstone'

# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/mycapstone'
