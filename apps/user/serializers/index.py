from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


# Main Section
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "is_admin")


class UserTokenSerializer(ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "email", "is_admin", "access_token")

    def get_access_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh.access_token)
