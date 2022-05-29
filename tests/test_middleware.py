from unittest.mock import MagicMock

from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from rest_framework.exceptions import ValidationError

from drf_impersonate.middleware import ImpersonationMiddleware

User = get_user_model()


class TestMiddleware(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.impersonater = baker.make(
            "auth.User", is_superuser=True, username="superuser"
        )
        cls.impersonatee = baker.make("auth.User", username="normaluser")

    def setUp(self):
        super().setUp()
        self.get_response = MagicMock()
        self.request = MagicMock()
        self.request.user = self.impersonater
        self.request.META = {}

    def test_GIVEN_no_impersonation_id_in_headers_THEN_request_user_is_not_modified(
        self,
    ):
        # GIVEN/WHEN
        middleware = ImpersonationMiddleware(self.get_response)
        middleware(self.request)

        # THEN
        self.assertEqual(self.request.user, self.impersonater)
        self.assertFalse(hasattr(self.request.user, "impersonator"))

    def test_GIVEN_wrong_impersonation_id_in_headers_THEN_validation_error_is_being_raised(
        self,
    ):
        # GIVEN/WHEN
        self.request.META["impersonate_id"] = 5
        middleware = ImpersonationMiddleware(self.get_response)

        # THEN
        with self.assertRaisesMessage(ValidationError, "User with id 5 does not exist"):
            middleware(self.request)

    def test_GIVEN_impersonation_id_in_headers_WHEN_can_impersonate_user_is_set_to_false_THEN_request_user_is_not_modified(  # noqa
        self,
    ):
        # GIVEN/WHEN
        self.request.META["impersonate_id"] = self.impersonatee.id
        self.request.user.can_impersonate_user = False
        middleware = ImpersonationMiddleware(self.get_response)
        middleware(self.request)

        # THEN
        self.assertEqual(self.request.user, self.impersonater)
        self.assertFalse(hasattr(self.request.user, "impersonator"))

    def test_GIVEN_impersonation_id_in_headers_THEN_request_user_is_modified(self):
        # GIVEN/WHEN
        self.request.META["impersonate_id"] = self.impersonatee.id
        middleware = ImpersonationMiddleware(self.get_response)
        middleware(self.request)

        # THEN
        self.assertEqual(self.request.user, self.impersonatee)
        self.assertTrue(hasattr(self.request, "impersonator"))
        self.assertEqual(self.request.impersonator, self.impersonater)
