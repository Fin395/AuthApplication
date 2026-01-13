from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from users.models import User
from users.permissions import (
    IsAdminOrModerator,
    IsAdminOrModeratorOrProfileOwner,
    IsAdminOrProfileOwner,
)
from users.serializers import UserReducedSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrProfileOwner]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if (
            self.request.user.groups.filter(name=["Администратор"]).exists()
            or self.request.user == self.get_object()
        ):
            return UserSerializer
        else:
            return UserReducedSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrModerator]

    def get_serializer_class(self):
        if self.request.user.groups.filter(name="Администратор").exists():
            return UserSerializer
        else:
            return UserReducedSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrModeratorOrProfileOwner]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            auth_header = request.headers.get("Authorization", None)
            if not auth_header:
                return Response(
                    {"detail": "Authorization header not found."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token = auth_header.split()[1]

            OutstandingToken.objects.filter(token=token).delete()

            return Response(status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
