"""Middlewares for DRF Impersonate"""
import logging
from typing import Optional

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from rest_framework.exceptions import ValidationError

User = get_user_model()

logger = logging.getLogger(__name__)


class ImpersonationMiddleware:
    """Impersonation Middleware

    Middleware to handle impersonation requests.
    If we get a request with a valid impersonation_id in requests header, we will
    set the `request.user` to the user specified in the header.

    And we also set an extra attribute in request that is `request.impersonator` which
    is the user that is impersonating.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # impersonate the user
        self.impersonate(request)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def impersonate(self, request: HttpRequest) -> None:
        """Method to check and impersonate the user"""
        user: User = request.user
        impersonate_id: Optional[str]
        if not (impersonate_id := request.META.get("impersonate_id")):
            logger.debug("No impersonate_id found in request")
            return

        try:
            impersonated_user: User = User.objects.get(pk=impersonate_id)
        except User.DoesNotExist as e:
            raise ValidationError(
                {"msg": f"User with id {impersonate_id} does not exist"}
            ) from e

        # TODO: document this that end users should implement this attribute
        # check for `can_impersonate_user` attribute on User model
        if not getattr(user, "can_impersonate_user", True):
            # TODO: We should raise error if `impersonate_id` is there but can_impersonate_user is not set
            logger.debug("User cannot impersonate. User.can_impersonate_user is False")
            return

        setattr(request, "impersonator", user)
        setattr(request, "user", impersonated_user)
        logger.info(f"Impersonating user {impersonated_user}")
