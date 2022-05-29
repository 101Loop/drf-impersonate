from django.urls import include
from django.urls import path

from tests.views import ImpersonateView

urlpatterns = [
    path("", include("drf_impersonate.urls", namespace="drf_impersonate")),
    path("impersonate/", ImpersonateView.as_view(), name="impersonate"),
]
