from django.conf import settings

LANGUAGES = [code for code, name in settings.LANGUAGES]

LANGUAGES_CHOICES = settings.LANGUAGES
