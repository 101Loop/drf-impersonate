"""utils"""
from typing import Optional

from django.http import HttpRequest


def get_client_ip(request: HttpRequest) -> Optional[str]:
    """
    Get client ip address.
    """
    if x_forwarded_for := request.META.get("HTTP_X_FORWARDED_FOR"):
        return x_forwarded_for.split(",")[0]
    else:
        return request.META.get("REMOTE_ADDR")
