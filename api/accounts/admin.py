from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'language', 'time_zone',
                    'is_active', 'is_premium', 'is_staff', 'is_superuser')
    list_filter = ('language', 'is_active', 'is_premium', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'full_name')
    fields = ('id', 'email', 'full_name', 'username', 'language', 'time_zone',
              'platform', 'is_active', 'is_premium', 'is_staff', 'is_superuser',
              'emails_subscribed', 'emails_bounced', 'emails_complained')
    readonly_fields = ('id', 'is_superuser', 'emails_bounced', 'emails_complained')
    exclude = ('groups', 'user_permissions', 'password')

    def has_add_permission(self, request):
        return False
