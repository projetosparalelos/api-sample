from core.drf_jwt import jwt_get_user_from_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication as RFJJSONWebTokenAuthentication

from .utils import i18n_activate


class JSONWebTokenAuthentication(RFJJSONWebTokenAuthentication):
    def authenticate(self, request):
        authentication = super().authenticate(request)
        if authentication:
            user, payload = authentication
            i18n_activate(user, request=request)
        return authentication

    def authenticate_credentials(self, payload):
        return jwt_get_user_from_payload_handler(payload)
