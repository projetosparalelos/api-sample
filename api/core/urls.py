from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

from .views import APIRootView, VersionView

urlpatterns = [
    path('', APIRootView.as_view(), name='index'),
    path('version', VersionView.as_view(), name='version'),

    path('sitemap.xml', TemplateView.as_view(template_name='core/sitemap.xml', content_type='text/xml')),
    path('robots.txt', TemplateView.as_view(template_name='core/robots.txt', content_type='text/plain')),

    path('accounts/', include('accounts.urls')),
    path('legal/', include('legal.urls')),
    path('todo/', include('todo.urls')),
]

if settings.DEBUG or settings.DJANGO_ADMIN:
    from django.contrib import admin
    from django.contrib.auth.models import Group
    from rest_framework.documentation import include_docs_urls
    admin.site.site_header = admin.site.site_title = "Todo List API"
    admin.site.index_title = "Apps"
    admin.site.unregister(Group)
    urlpatterns.insert(0, path('admin/', admin.site.urls))
    urlpatterns.insert(1, path('docs/', include_docs_urls(title="Todo List API")))

if settings.DEBUG:  # pragma: no cover
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
