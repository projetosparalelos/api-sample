from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import User
from .validators import username_validator


class EmailField(serializers.EmailField):
    def to_internal_value(self, data):
        data = data.strip().lower()
        query = User.objects.filter(email=data)
        user = self.context.get('user', None)
        if user and user.is_authenticated:
            query = query.exclude(id=user.id)
        if query.exists():
            raise serializers.ValidationError(_("Email already registered."))
        return data


class UsernameField(serializers.CharField):
    def to_internal_value(self, data):
        data = data.strip().lower()
        username_validator(data)
        query = User.objects.filter(username=data)
        user = self.context.get('user', None)
        if user and user.is_authenticated:
            query = query.exclude(id=user.id)
        if query.exists():
            raise serializers.ValidationError(_("Username already exists."))
        return data


class UsernameOrEmailField(serializers.CharField):
    def to_internal_value(self, data):
        data = data.strip().lower()
        if '@' in data:
            user = User.objects.filter(email=data).first()
            if user:
                data = user.username
        return data
