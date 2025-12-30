from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
]
