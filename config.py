import os

# Gets the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    'AUTH0_DOMAIN' : 'agent88.us.auth0.com',
    'ALGORITHMS' : ['RS256'],
    'API_AUDIENCE' : 'stars'
    'CLIENT_ID'='xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ'
    'CLIENT_SECRET='euZkCMgG5Kq2gBRiB4zgiIi8p1-eNOZ2RhIuBOuynF2mLVQdjpWOHC7DnS74ZR5_'
    'AUTH0_CALLBACK_URL'='https://myapphsbk.herokuapp.com/'
}