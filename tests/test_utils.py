"""
test_drf-impersonate
------------

Tests for `drf-impersonate` utils module.
"""
from django.http import HttpRequest
from django.test import TestCase

from drf_impersonate.utils import get_client_ip


class TestUtils(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def test_meta_single_with_http_x_forwarded_for(self):
        """Check get_client_ip returns first item from HTTP_X_FORWARDED_FOR"""
        request = HttpRequest()
        request.META = {
            "HTTP_X_FORWARDED_FOR": "177.139.233.139, 198.84.193.157, 198.84.193.158",
        }
        result = get_client_ip(request)
        self.assertEqual(result, "177.139.233.139")

    def test_meta_single_with_remote_addr(self):
        """Check get_client_ip returns first item from HTTP_X_FORWARDED_FOR"""
        request = HttpRequest()
        request.META = {
            "REMOTE_ADDR": "198.84.193.158",
        }
        result = get_client_ip(request)
        self.assertEqual(result, "198.84.193.158")

    def test_meta_multi(self):
        """
        Check get_client_ip returns ip from HTTP_X_FORWARDED_FOR when
        HTTP_X_FORWARDED_FOR and REMOTE_ADDR is present
        """
        request = HttpRequest()
        request.META = {
            "HTTP_X_FORWARDED_FOR": "177.139.233.139, 198.84.193.157, 198.84.193.158",
            "REMOTE_ADDR": "177.139.233.133",
        }
        result = get_client_ip(request)
        self.assertEqual(result, "177.139.233.139")
