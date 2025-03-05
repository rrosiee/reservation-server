from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import User


# Main Section
class AuthSignupSerializer(ModelSerializer):
    admin_code = serializers.CharField(
        allow_null=True, allow_blank=True, required=False
    )

    class Meta:
        model = User
        fields = ("email", "password", "admin_code")

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("이미 가입된 이메일입니다.")
        return value

    def validate_admin_code(self, value):
        if value and value != "abcd":
            raise ValidationError("어드민 코드가 불일치합니다.")
        return value

    def create(self, validated_data):
        instance = User.objects.signup_user(**validated_data)
        return instance
