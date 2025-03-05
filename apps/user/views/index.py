from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.user.models import User
from apps.user.serializers import (
    UserSerializer,
)


# Main Section
class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializers = {
        "default": UserSerializer,
    }

    @swagger_auto_schema(
        tags=["User - 사용자"],
        operation_id="내 정보 조회",
        operation_description="",
        responses={200: UserSerializer()},
    )
    @action(detail=False, methods=["get"])
    def me(self, request):
        user = request.user
        return Response(
            data=UserSerializer(instance=user).data, status=status.HTTP_200_OK
        )
