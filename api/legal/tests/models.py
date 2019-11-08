from unittest.mock import patch

from ckeditor.fields import RichTextField
from core.models import LanguageModel, UUIDModel
from django.db import models
from django.test import TestCase

from ..models import Legal


@patch('legal.models._', side_effect=lambda s: s)
class LegalModelTests(TestCase):
    def setUp(self):
        self.model = Legal

    def test_subclass(self, _):
        self.assertTrue(issubclass(self.model, LanguageModel))
        self.assertTrue(issubclass(self.model, UUIDModel))

    def test_meta(self, _):
        self.assertEqual(self.model._meta.verbose_name, 'legal')
        self.assertEqual(self.model._meta.verbose_name_plural, 'legal')

    def test_ABOUT(self, _):
        self.assertEqual(self.model.ABOUT, 'about')

    def test_PRIVACY(self, _):
        self.assertEqual(self.model.PRIVACY, 'privacy')

    def test_TERMS(self, _):
        self.assertEqual(self.model.TERMS, 'terms')

    def test_TYPE_CHOICES(self, _):
        self.assertEqual(self.model.TYPE_CHOICES, (
            (self.model.ABOUT, "About"),
            (self.model.PRIVACY, "Privacy"),
            (self.model.TERMS, "Terms"),
        ))

    def test_type(self, _):
        field = self.model._meta.get_field('type')
        self.assertEqual(type(field), models.CharField)
        self.assertEqual(field.max_length, 16)
        self.assertEqual(field.choices, self.model.TYPE_CHOICES)
        self.assertEqual(field.verbose_name, "type")

    def test_title(self, _):
        field = self.model._meta.get_field('title')
        self.assertEqual(type(field), models.CharField)
        self.assertEqual(field.max_length, 256)
        self.assertEqual(field.verbose_name, "title")

    def test_content(self, _):
        field = self.model._meta.get_field('content')
        self.assertEqual(type(field), RichTextField)
        self.assertEqual(field.verbose_name, "content")

    def test__str__(self, _):
        legal = self.model(title='foo bar')
        self.assertEqual(str(legal), 'foo bar')
