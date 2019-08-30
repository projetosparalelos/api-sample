import bugsnag
import pytz
from django.contrib.auth.middleware import get_user
from django.utils import timezone, translation
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .time_zones import TIME_ZONES


def bugsnag_notify(exception_message, meta_data):
    bugsnag.notify(Exception(exception_message), meta_data=meta_data or {})


def get_grouped_time_zones():
    """
    Return time zones grouped by their offsets.
    {
        -4: ['America/New_York'],
        -3: ['America/Argentina/Buenos_Aires', 'America/Sao_Paulo'],
        ...
    }
    """
    grouped_time_zones = {}
    utc_now = timezone.now()
    for tz in TIME_ZONES:
        utc_offset = utc_now.astimezone(timezone.pytz.timezone(tz)).utcoffset().total_seconds() / 60 / 60
        if utc_offset not in grouped_time_zones:
            grouped_time_zones[utc_offset] = []
        grouped_time_zones[utc_offset].append(tz)
    return grouped_time_zones


def get_request_user(request):
    user = get_user(request)
    if user.is_authenticated:
        return user
    jwt_authentication = JSONWebTokenAuthentication()
    if jwt_authentication.get_jwt_value(request):
        user, jwt = jwt_authentication.authenticate(request)
    return user


def i18n_activate(user, request=None):
    translation.activate(user.language)
    if request:
        request.LANGUAGE_CODE = user.language
    if user.time_zone:
        timezone.activate(pytz.timezone(user.time_zone))
    else:
        timezone.deactivate()
