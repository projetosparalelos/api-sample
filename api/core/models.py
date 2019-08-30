import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("id"))
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("created"))

    class Meta:
        abstract = True


class LanguageModel(models.Model):
    language = models.CharField(db_index=True, max_length=16, choices=settings.LANGUAGES, verbose_name=_("language"))

    class Meta:
        abstract = True
