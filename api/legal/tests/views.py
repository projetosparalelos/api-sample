from unittest.mock import MagicMock, patch

from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.test import APIClient, APITestCase
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Legal
from ..serializers import LegalSerializer
from ..views import LegalDetailView


class LegalDetailViewTests(APITestCase):
    def setUp(self):
        self.view_class = LegalDetailView
        self.view = LegalDetailView.as_view({'get': 'retrieve'})

    def test_subclass(self):
        self.assertTrue(issubclass(self.view_class, ReadOnlyModelViewSet))

    def test_permission_classes(self):
        self.assertEqual(self.view_class.permission_classes, (AllowAny,))

    def test_queryset(self):
        self.assertQuerysetEqual(self.view_class.queryset, Legal.objects.all())

    def test_serializer_class(self):
        self.assertEqual(self.view_class.serializer_class, LegalSerializer)

    @patch('legal.views.get_legal')
    def test_get_object(self, get_legal):
        get_legal.return_value = 'some data'
        view = self.view_class()
        request = MagicMock()
        view.request = request
        view.kwargs = {'type': 'about'}
        obj = view.get_object()
        self.assertEqual(obj, 'some data')
        get_legal.assert_called_once_with(request.LANGUAGE_CODE, 'about')

    @patch('legal.views.get_legal')
    def test_get(self, get_legal):
        get_legal.return_value = Legal(
            language=settings.LANGUAGE_CODE,
            type=Legal.ABOUT,
            title='foo',
            content='bar'
        )
        client = APIClient()
        response = client.get('/legal/legal/about/')
        self.assertEqual(response.data, {
            'type': Legal.ABOUT,
            'language': settings.LANGUAGE_CODE,
            'title': 'foo',
            'content': 'bar'
        })
