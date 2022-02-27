from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="title_name",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
    ),
    validators=["flex"],
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path(
        r"swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        r"swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        r"redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-v1"
    ),
    path("admin/", admin.site.urls),
    path("", include('project_name.apps.users.urls')),
]
