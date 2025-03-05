from django.shortcuts import redirect
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from apps.user.views import AuthViewSet, UserViewSet

# Swagger 문서 관련 API
schema_view = get_schema_view(
    openapi.Info(
        title="시험 일정 예약 시스템 API",
        default_version="",
        description="미구현 사항 : 유저 비밀번호 변경, admin_code를 동적으로 조정하는 것",
        contact=openapi.Contact(email="offbeat1020@naver.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_urlpatterns = [
    # 루트 URL 접속 시 /api/docs로 리다이렉트
    path("", lambda request: redirect("/api/docs/", permanent=True)),
    # Swagger UI 및 API 문서 경로
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    re_path(
        r"^api/docs(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]

# API 관련 URL
router = routers.SimpleRouter(trailing_slash=False)

# Auth
router.register(r"auth", AuthViewSet, basename="auth")

# User
router.register(r"user", UserViewSet, basename="user")

api_urlpatterns = [
    path("api/", include(router.urls)),
]

# 최종 URL 패턴 설정
urlpatterns = swagger_urlpatterns + api_urlpatterns
