#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_drf-impersonate
------------

Tests for `drf-impersonate` models module.
"""
from django.test import TestCase

from drf_impersonate import models


class TestDrf_impersonate(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def test_something(self):
        pass
