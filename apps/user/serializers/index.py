from rest_framework.serializers import ModelSerializer

from apps.user.models import User


# Main Section
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "is_admin")
