from django.contrib.auth.middleware import AuthenticationMiddleware as DjangoAuthenticationMiddleware

from .utils import i18n_activate


class AuthenticationMiddleware(DjangoAuthenticationMiddleware):
    def process_request(self, request):
        super().process_request(request)
        if request.user.is_authenticated:
            i18n_activate(request.user, request=request)
