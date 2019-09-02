from django.conf import settings
from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedOrDocs(IsAuthenticated):
    def has_permission(self, request, view):
        docs_url = '/{}'.format(settings.BASE_DOCS_URL)
        if (settings.DEBUG or settings.DJANGO_ADMIN) and request.path.startswith(docs_url):
            return True
        return super().has_permission(request, view)
