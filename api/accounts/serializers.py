from core.drf_jwt import create_token, jwt_get_user_from_payload_handler
from core.languages import LANGUAGES
from core.time_zones import TIME_ZONES
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_jwt.serializers import (
    RefreshJSONWebTokenSerializer as RFJRefreshJSONWebTokenSerializer,
    VerificationBaseSerializer as RFJVerificationBaseSerializer,
)

from .fields import EmailField, UsernameField, UsernameOrEmailField
from .validators import password_validator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = EmailField(label=_("email"), help_text=_("Email"))
    username = UsernameField(label=_("username"), help_text=_("Username"))
    short_name = serializers.SerializerMethodField(label=_("short name"), help_text=_("Short name"))
    check_password = serializers.CharField(required=False, write_only=True,
                                           label=_("check password"), help_text=_("Check password"))

    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'short_name', 'username', 'language', 'time_zone',
                  'is_premium', 'is_staff', 'emails_subscribed', 'platform',
                  'password', 'check_password']
        read_only_fields = ('username', 'is_premium', 'is_staff')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'validators': [password_validator]
            }
        }

    def get_short_name(self, obj):
        return obj.get_short_name()

    def validate_check_password(self, value):
        if not self.context['user'].check_password(value):
            raise serializers.ValidationError(_("Wrong current password."))
        return value

    def validate(self, data):
        if 'check_password' not in data and ('username' in data or 'email' in data or 'password' in data):
            raise serializers.ValidationError(_("Current password must be provided."))
        return data

    def save(self):
        with transaction.atomic():
            instance = super().save()
            if 'password' in self.validated_data:
                instance.set_password(self.validated_data['password'])
                instance.save(update_fields=['password'])
            return instance


class SignUpSerializer(serializers.Serializer):
    # In
    email = EmailField(required=True, write_only=True, label=_("email"), help_text=_("Email"))
    full_name = serializers.CharField(required=True, write_only=True, label=_("full name"), help_text=_("Full name"))
    username = UsernameField(required=True, write_only=True, label=_("username"), help_text=_("Username"))
    password = serializers.CharField(required=True, write_only=True,
                                     style={'input_type': 'password'}, validators=[password_validator],
                                     label=_("password"), help_text=_("Password"))
    language = serializers.ChoiceField(required=True, write_only=True, choices=LANGUAGES,
                                       label=_("language"), help_text=_("Language"))
    time_zone = serializers.ChoiceField(required=True, write_only=True, choices=TIME_ZONES,
                                        label=_("time zone"), help_text=_("Time zone"))
    platform = serializers.ChoiceField(required=True, write_only=True, choices=User.PLATFORM_CHOICES,
                                       label=_("platform"), help_text=_("Platform"))

    # Out
    access_token = serializers.CharField(read_only=True, label=_("JWT token"), help_text=_("JWT token"))

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return {'access_token': create_token(user)}


class LogInSerializer(serializers.Serializer):
    # In
    username = UsernameOrEmailField(required=True, write_only=True,
                                    label=_("username"), help_text=_("Username or email"))
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'},
                                     label=_("password"), help_text=_("Password"))

    # Out
    access_token = serializers.CharField(read_only=True, label=_("JWT token"), help_text=_("JWT Token"))

    def validate(self, data):
        user = auth.authenticate(username=data['username'].lower(), password=data['password'])
        if user:
            return {'access_token': create_token(user)}
        raise serializers.ValidationError(_("Wrong username/email or password."))


class VerificationBaseSerializer(RFJVerificationBaseSerializer):
    """This serializer has been overritten so that username is not mandatory in the JWT token."""
    def _check_user(self, payload):
        return jwt_get_user_from_payload_handler(payload)


class RefreshJSONWebTokenSerializer(VerificationBaseSerializer, RFJRefreshJSONWebTokenSerializer):
    """This serializer has been overritten so that username is not mandatory in the JWT token."""
    pass


class CheckUsernameSerializer(serializers.Serializer):
    username = UsernameField(required=True, label=_("username"))
