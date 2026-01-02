from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_again = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if 'password' in data and 'password_again' in data:
            if data['password'] != data['password_again']:
                raise serializers.ValidationError('Пароли не совпадают')
            else:
                pass
            data.pop('password_again')
        return data


class UserReducedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "is_staff"]
