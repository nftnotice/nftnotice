from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("app_nftnotice/", include("app_nftnotice.urls")),
    path("admin/", admin.site.urls),
]
