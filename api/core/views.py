from collections import OrderedDict

from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import VersionSerializer


class APIRootView(views.APIView):
    schema = None
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        urls = OrderedDict()
        urls['accounts'] = request.build_absolute_uri('/accounts/')
        urls['legal'] = request.build_absolute_uri('/legal/')
        urls['todo'] = request.build_absolute_uri('/todo/')
        urls['version'] = request.build_absolute_uri(reverse('version'))
        return Response(urls)


class VersionView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VersionSerializer

    def get_object(self):
        return {}
