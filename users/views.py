from rest_framework import generics
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
