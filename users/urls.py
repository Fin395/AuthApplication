from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.mock_views import (HomeworkMockCreateAPIView,
                              HomeworkMockDestroyAPIView,
                              HomeworkMockRetrieveAPIView,
                              HomeworkMockUpdateAPIView)
from users.views import (LogoutView, UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("user/register/", UserCreateAPIView.as_view(), name="user-register"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-get"),
    path("user/users/", UserListAPIView.as_view(), name="user-list"),
    path("user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("user/logout/", LogoutView.as_view(), name="user-logout"),
    path("homework/create/", HomeworkMockCreateAPIView.as_view(), name="homework-mock"),
    path(
        "homework/update/<int:homework_id>/",
        HomeworkMockUpdateAPIView.as_view(),
        name="homework-update",
    ),
    path(
        "homework/<int:homework_id>/",
        HomeworkMockRetrieveAPIView.as_view(),
        name="homework-get",
    ),
    path(
        "homework/delete/<int:homework_id>/",
        HomeworkMockDestroyAPIView.as_view(),
        name="homework-delete",
    ),
]
