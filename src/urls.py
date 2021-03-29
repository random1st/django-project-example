from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.response import Response
from rest_framework.views import APIView

from api.routers.v1 import api_urlpatterns as api_v1


class VersionView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        return Response({"version": settings.APP_VERSION})


base_urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check/", include("health_check.urls")),
    path("", VersionView.as_view()),
]

urlpatterns = base_urlpatterns + [
    re_path(r'^api/(?P<version>v1)/', include(api_v1)),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(title="API", default_version="v1", ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path("docs/", include_docs_urls(title="API")),
        url(
            r"^(?P<version>v1)/swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0, ),
            name="API-json",
        ),
        url(
            r"^(?P<version>v1|v1.1|v2)/swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="API-swagger-ui",
        ),
        url(
            r"^(?P<version>v1|v1.1|v2)/redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="API-redoc",
        ),
    ]
