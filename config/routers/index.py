from django.shortcuts import redirect
from django.urls import path, re_path, reverse_lazy
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework.authtoken.views import ObtainAuthToken

# Swagger API 문서 설정
schema_view = get_schema_view(
    openapi.Info(
        title="시험 일정 예약 시스템 API",
        default_version="v1",
        description="""
            본 API는 프로그래머스가 운영하는 온라인 시험 플랫폼에서 기업 고객이 채용 시험 일정을 
            효율적으로 예약할 수 있도록 지원하는 시스템입니다.
        """,
        contact=openapi.Contact(email="offbeat1020@naver.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Router 설정
router = routers.SimpleRouter(trailing_slash=False)

# URL 패턴
urlpatterns = [
    path("auth/token/", ObtainAuthToken.as_view()),  # 인증 토큰

    # Swagger API 문서
    path("", lambda request: redirect(reverse_lazy("schema-swagger-ui"), permanent=True)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^docs(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]

# Router의 URL 추가
urlpatterns += router.urls
