from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .models import Legal


def get_legal(language, type):
    cache_key = 'legal__cache__get_legal-{}-{}'.format(language, type)
    legal = cache.get(cache_key)
    if not legal:
        legal = get_object_or_404(Legal, language__iexact=language, type=type)
        cache.set(cache_key, legal)
    return legal
