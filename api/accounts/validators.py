import re

from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


def username_validator(value):
    value_len = len(value)
    if 6 <= value_len <= 32 and re.match(r'^[a-z0-9]+[_\.]?[a-z0-9]+$', value):
        return value
    raise serializers.ValidationError(_(
        "Username must be between 6 and 32 characters in length and contain only "
        "unaccented lowercase letters, numbers and . or _ in the middle."))


def password_validator(value):
    password_validation.validate_password(password=value)
    return value
