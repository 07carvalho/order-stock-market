from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="GitHub Service",
        default_version="v1",
        description="Test description",
        contact=openapi.Contact(email="felipe.carvalho07@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/orders/", include("orders.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0)),
]
