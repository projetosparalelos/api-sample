from calendar import timegm
from datetime import datetime

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    payload = {
        'user_id': str(user.pk),
        'is_staff': user.is_staff,
        'is_premium': user.is_premium,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(datetime.utcnow().utctimetuple())
    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    return {'access_token': token}


def jwt_get_user_secret_key(user):
    return user.jwt_secret_key


def jwt_get_user_from_payload_handler(payload):
    User = get_user_model()
    user_id = payload.get('user_id')
    if not user_id:
        raise exceptions.AuthenticationFailed(_('Invalid payload.'))
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise exceptions.AuthenticationFailed(_('Invalid signature.'))
    if not user.is_active:
        raise exceptions.AuthenticationFailed(_('User account is disabled.'))
    return user


def create_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token
