"""Example URL Configuration"""
from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("drf_impersonate.urls", namespace="drf_impersonate")),
]
