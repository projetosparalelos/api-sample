from django.contrib import admin

from .models import List, Task


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)
    search_fields = ('user__full_name', 'user__email', 'name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'list', 'name', 'due_date', 'due_time', 'done')
    list_filter = ('list', 'due_date', 'done')
    search_fields = ('user__full_name', 'user__email', 'name')
