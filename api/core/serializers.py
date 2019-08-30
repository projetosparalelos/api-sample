from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class VersionSerializer(serializers.Serializer):
    version = serializers.SerializerMethodField(label=_("version"), help_text=_("Version"))

    def get_version(self, obj):
        return settings.VERSION
