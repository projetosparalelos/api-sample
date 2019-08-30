from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LegalConfig(AppConfig):
    name = 'legal'
    label = 'legal'
    verbose_name = _("Legal")
