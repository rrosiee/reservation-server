from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import (
    AuthSignupSerializer,
    UserSerializer,
    UserTokenSerializer,
    AuthLoginSerializer,
)


# Main Section
class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializers = {
        "default": AuthSignupSerializer,
    }
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        tags=["Auth - 인증"],
        operation_id="회원가입",
        operation_description="`admin_code` : 어드민 코드를 abcd로 할 경우 어드민 계정으로 회원가입이 가능합니다.",
        request_body=AuthSignupSerializer,
        responses={201: UserSerializer()},
    )
    @action(detail=False, methods=["POST"], url_name="signup")
    def signup(self, request, *args, **kwargs):
        serializer = AuthSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            data=UserSerializer(instance=instance).data, status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        tags=["Auth - 인증"],
        operation_id="로그인",
        operation_description="",
        request_body=AuthLoginSerializer,
        responses={200: UserTokenSerializer()},
    )
    @action(detail=False, methods=["POST"], url_name="login")
    def login(self, request, *args, **kwargs):
        serializer = AuthLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return Response(data=UserTokenSerializer(user).data, status=status.HTTP_200_OK)
