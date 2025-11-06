import jwt
from datetime import datetime, timedelta, UTC
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = 'HS256'

# PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
# ... ta clé privée RSA ...
# -----END RSA PRIVATE KEY-----"""

# PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
# ... la clé publique correspondante ...
# -----END PUBLIC KEY-----"""


def generate_nats_jwt(username):
    now = datetime.now(UTC)
    payload = {
        'sub': username,
        'exp': now + timedelta(hours=1),
        'iat': now,
        'nats': {
            'permissions': {
                'publish': ['updates.*'],
                'subscribe': ['events.*'],
            }
        },
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
