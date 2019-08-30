from django.contrib import admin

from .models import Legal


@admin.register(Legal)
class LegalAdmin(admin.ModelAdmin):
    list_display = ('language', 'type', 'title')
    list_filter = ('language', 'type')
