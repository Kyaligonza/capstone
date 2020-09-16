import json
from flask import request, _request_ctx_stack
from functools import wraps
import os
from urllib.request import urlopen
from jose import jwt
# from os import environ
# from config import auth0_config


AUTH0_DOMAIN = 'agent88.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'stars'
# CLIENT_ID  = 'xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ'

# SECRET_KEY='GodLove'

# AUTH0_DOMAIN = 'agency99.us.auth0.com'
# ALGORITHMS = ['RS256']
# API_AUDIENCE = 'actors'


# AUTH0_DOMAIN = auth0_config['AUTH0_DOMAIN']
# ALGORITHMS = auth0_config['ALGORITHMS']
# API_AUDIENCE = auth0_config['API_AUDIENCE']
# CLIENT_ID = auth0_config['CLIENT_ID']
# CLIENT_SECRET = auth0_config['CLIENT_SECRET']

# AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
# ALGORITHMS = os.environ.get('ALGORITHMS')
# API_AUDIENCE = os.environ.get('API_AUDIENCE')
# CLIENT_ID = os.environ.get('CLIENT_ID')
# CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header

'''
@Done implement get_token_auth_header() method
    it should attempt to get the header from the request
    it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
    it should raise an AuthError if the header is malformed
    return the token part of the header
'''
import http.client

conn = http.client.HTTPSConnection("agent88.us.auth0.com")

payload = "{\"client_id\":\"xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ\",\"client_secret\":\"euZkCMgG5Kq2gBRiB4zgiIi8p1-eNOZ2RhIuBOuynF2mLVQdjpWOHC7DnS74ZR5_\",\"audience\":\"stars\",\"grant_type\":\"client_credentials\"}"
# payload ="{\"client_id\":\"{}\".format(CLIENT_ID),\"client_secret\":\"{}\".format(CLIENT_SECRET),\"audience\":\"stars\",\"grant_type\":\"client_credentials\"}"
# payload = "{\"client_id\":\"xFoG8R71EEFXmHIOKPxGLpdTQCG2iZVZ\",\"client_secret\":\"euZkCMgG5Kq2gBRiB4zgiIi8p1-eNOZ2RhIuBOuynF2mLVQdjpWOHC7DnS74ZR5_\",\"audience\":\"stars\"}"
headers = { "content-type": "application/json" }

conn.request("POST", "/oauth/token", payload, headers)
res = conn.getresponse()
data = res.read()
data1 = data.decode("utf-8")
result = json.loads(data1)
# result = requests.post(url,
    #   headers={'Content-Type':'application/json',
            #    'Authorization': 'Bearer {}'.format(access_token)})
# print(data.decode("utf-8"))
# tokenx = res.headers.get("access-token")
access_token = result['access_token']
# print(result['access_token'])


def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    # auth = {'Authorization': 'Bearer {}'.format(access_token)}
    auth ='Bearer {}'.format(access_token)
    # auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        }, 401)

    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start with "Bearer".'
        }, 401)

    elif len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)

    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    token = parts[1]
    return token
#    raise Exception('Not Implemented')


'''
@Done implement check_permissions(permission, payload) method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

        it should raise an AuthError if permissions
        are not included in the payload
        !!NOTE check your RBAC settings in Auth0
        it should raise an AuthError if the requested permission
        string is not in the payload permissions array
        return true otherwise
'''


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permissions not included in JWT.'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found.'
        }, 403)
    return True
    # raise Exception('Not Implemented')


'''
@Done implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload

    !!NOTE urlopen has a common certificate error described here:
    https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
'''


def verify_decode_jwt(token):

    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims.Please, check the audience and issuer.'  # noqa
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)

    # raise Exception('Not Implemented')


'''
@Done implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        it should use the get_token_auth_header method to get the token
        it should use the verify_decode_jwt method to decode the jwt
        it should use the check_permissions method validate
        claims and check the requested permission
        return the decorator which passes the decoded payload
        to the decorated method
'''

# def requires_auth(permission=''):
#     def requires_auth_decorator(f):
#         @wraps(f)
#         def wrapper(*args, **kwargs):
#             token = get_token_auth_header()
#             try:
#                 payload = verify_decode_jwt(token)
#             except Exception:
#                 abort(401)

#             check_permissions(permission, payload)
#             return f(payload, *args, **kwargs)

#         return wrapper
#     return requires_auth_decorator

def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
