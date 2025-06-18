from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

from apps.authentication.infrastructure.models import CustomUser

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get("email"),
            "password": attrs.get("password")
        }

        user = User.objects.filter(email=credentials[self.username_field]).first()
        if user is None or not user.check_password(credentials["password"]):
            raise AuthenticationFailed("Invalid credentials")

        return super().validate(attrs)


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user