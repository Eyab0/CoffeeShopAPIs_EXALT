from jwt import encode
from datetime import timedelta, datetime
from services.backend.config import config


def generate_access_token(employee):
    """
    generate access access_token
    :return: encoded access access_token
    """
    payload = {
        "username": employee.username,
        "role": employee.role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    return encode(payload, config.PRIVATE_KEY, algorithm=config.ALGORITHM)
