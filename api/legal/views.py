from collections import OrderedDict

from rest_framework import views, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .cache import get_legal
from .models import Legal
from .serializers import LegalSerializer


class APIRootView(views.APIView):
    schema = None

    def get(self, request, *args, **kwargs):
        urls = OrderedDict()
        urls['legal'] = request.build_absolute_uri(
            reverse('legal:legal-list'))
        urls['legal-about'] = request.build_absolute_uri(
            reverse('legal:legal-detail', kwargs={'type': Legal.ABOUT}))
        urls['legal-privacy'] = request.build_absolute_uri(
            reverse('legal:legal-detail', kwargs={'type': Legal.PRIVACY}))
        urls['legal-terms'] = request.build_absolute_uri(
            reverse('legal:legal-detail', kwargs={'type': Legal.TERMS}))
        return Response(urls)


class LegalDetailView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Legal.objects.all()
    lookup_field = 'type'
    serializer_class = LegalSerializer

    def get_object(self):
        return get_legal(self.request.LANGUAGE_CODE, self.kwargs['type'])
