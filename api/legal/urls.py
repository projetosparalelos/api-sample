from django.urls import path
from rest_framework import routers

from . import views

app_name = 'legal'

router = routers.DefaultRouter()
router.register(r'legal', views.LegalDetailView, basename='legal')

urlpatterns = [
    path('', views.APIRootView.as_view(), name='index'),
] + router.urls
