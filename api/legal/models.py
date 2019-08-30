from ckeditor.fields import RichTextField
from core.models import LanguageModel, UUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Legal(UUIDModel, LanguageModel):
    ABOUT = 'about'
    PRIVACY = 'privacy'
    TERMS = 'terms'
    TYPE_CHOICES = (
        (ABOUT, _("About")),
        (PRIVACY, _("Privacy")),
        (TERMS, _("Terms")),
    )

    type = models.CharField(max_length=16, choices=TYPE_CHOICES, verbose_name=_("type"))
    title = models.CharField(max_length=256, verbose_name=_("title"))
    content = RichTextField(verbose_name=_("content"))

    class Meta:
        verbose_name = _("legal")
        verbose_name_plural = _("legal")

    def __str__(self):
        return self.title
