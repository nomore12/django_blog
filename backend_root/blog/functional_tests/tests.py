import os
from django.test import TestCase
from django.contrib.staticfiles.testing import (
    StaticLiveServerTestCase,
    LiveServerTestCase,
)
from selenium import webdriver
from posts.models import Post
from pathlib import Path


class PostHttpTestCase(StaticLiveServerTestCase):
    """
    기능 테스트.
    셀레니움으로 가상 테스트가 가능하도록 함.
    """

    def setUp(self):
        driver_path = f"{Path().resolve()}/chromedriver"
        print(driver_path)
        self.browser = webdriver.Chrome(driver_path)

    def tearDown(self):
        self.browser.quit()

    def test_default_page_can_connect(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Django", self.browser.title)
