from rest_framework import serializers

from apps.user.models import User


# Main Section
class AuthLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # 사용자 조회
        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError("이메일 또는 비밀번호가 올바르지 않습니다.")

        # 비밀번호 검증
        if not user.check_password(password):
            raise serializers.ValidationError("이메일 또는 비밀번호가 올바르지 않습니다.")

        # 검증 성공 시 user 반환
        data["user"] = user
        return data
