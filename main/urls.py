
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="base project",
        default_version="v1",
        description="API For Base Projects",
        contact=openapi.Contact(email="daffy@saungseo.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/profiles/', include("core.profiles.urls")),
    path('api/v1/auth/', include("djoser.urls")),
    path('api/v1/auth/', include("djoser.urls.jwt")),
]
