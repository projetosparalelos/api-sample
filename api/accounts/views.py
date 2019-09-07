from collections import OrderedDict

from rest_framework import views, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import AutoSchema
from rest_framework_jwt.views import JSONWebTokenAPIView

from .serializers import (
    CheckUsernameSerializer, LogInSerializer, RefreshJSONWebTokenSerializer, SignUpSerializer, UserSerializer,
)


class APIRootView(views.APIView):
    schema = None

    def get(self, request, *args, **kwargs):
        urls = OrderedDict()
        urls['sign-up'] = request.build_absolute_uri(reverse('accounts:sign_up'))
        urls['log-in'] = request.build_absolute_uri(reverse('accounts:log_in'))
        urls['refresh-token'] = request.build_absolute_uri(reverse('accounts:refresh_token'))
        urls['check-username'] = request.build_absolute_uri(reverse('accounts:check_username'))
        urls['me'] = request.build_absolute_uri(reverse('accounts:me'))
        return Response(urls)


class SignUpView(CreateAPIView):
    schema = AutoSchema()

    """
    Sign up an user and return a JWT token.
    """
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer


class LogInView(CreateAPIView):
    schema = AutoSchema()

    """
    Log in an user and return a JWT token.
    """
    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    def perform_create(self, serializer):
        pass  # Override to not do anything.


class RefreshJSONWebToken(JSONWebTokenAPIView):
    schema = AutoSchema()

    """
    Returns a refreshed token with new expiration based on existing token.
    """
    serializer_class = RefreshJSONWebTokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Retrieve or partial update user data.
    """
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(user=self.request.user if self.request else None)
        return context


class CheckUsernameView(CreateAPIView):
    schema = AutoSchema()

    """
    Check is a username is available for use.
    """
    permission_classes = (AllowAny,)
    serializer_class = CheckUsernameSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(user=self.request.user if self.request else None)
        return context

    def perform_create(self, serializer):
        pass  # Override to not do anything.
