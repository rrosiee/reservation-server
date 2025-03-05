from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import AuthSignupSerializer, UserSerializer


# Main Section
class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializers = {
        "default": AuthSignupSerializer,
    }

    @swagger_auto_schema(
        operation_summary="회원가입 API",
        operation_description="이메일을 사용하여 회원가입을 진행합니다.",
        request_body=AuthSignupSerializer,  # 응답 데이터
        responses={201: UserSerializer()},
    )
    @action(detail=False, methods=["POST"], url_name="signup")
    def signup(self, request):
        serializer = AuthSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(UserSerializer(instance=instance).data)
