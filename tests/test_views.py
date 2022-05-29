from django.test import TestCase
from model_bakery import baker


class TestImpersonation(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.impersonater = baker.make("auth.User", is_superuser=True)
        cls.impersonatee = baker.make(
            "auth.User",
        )
        cls.api_url = "/impersonate/"

    def setUp(self):
        super().setUp()

    def test_request_user_is_impersonatee(self):
        self.client.force_login(self.impersonater)
        headers = {"impersonate_id": self.impersonatee.id}
        response = self.client.post(self.api_url, **headers)
        self.assertEqual(response.status_code, 200)
