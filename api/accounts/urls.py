from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.APIRootView.as_view(), name='index'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('log-in/', views.LogInView.as_view(), name='log_in'),
    path('refresh-token/', views.RefreshJSONWebToken.as_view(), name='refresh_token'),
    path('check-username/', views.CheckUsernameView.as_view(), name='check_username'),
    path('me/', views.UserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}), name='me'),
]
