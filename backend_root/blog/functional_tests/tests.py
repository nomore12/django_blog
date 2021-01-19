import os
from django.test import TestCase
from django.contrib.staticfiles.testing import (
    StaticLiveServerTestCase,
    LiveServerTestCase,
)
from selenium import webdriver
from posts.models import Post
from pathlib import Path
import time


class PostHttpTestCase(StaticLiveServerTestCase):
    """
    기능 테스트.
    셀레니움으로 가상 테스트가 가능하도록 함.
    """

    def setUp(self):
        # browser.get()이 호출될때마다 실행
        driver_path = f"{Path().resolve()}/chromedriver"
        self.browser = webdriver.Chrome(driver_path)
        for post in range(5):
            Post.objects.create(title=f"{post}' post")
        time.sleep(1)
        print(Post.objects.count())

    def tearDown(self):
        self.browser.quit()

    def test_default_page_can_connect(self):
        # 포스트 페이지 기본적인 테스트
        post_url = f"{self.live_server_url}/post/"
        self.browser.get(post_url)
        post_list = self.browser.find_element_by_class_name("post_list")
        self.assertEqual(post_list.tag_name, "ol")
        lists = post_list.find_elements_by_class_name("post_title")
        self.assertEqual(len(lists), Post.objects.all().count())

        #  모든 포스트를 순회하며 테스트.
        for a in lists:
            href = a.get_attribute("href")
            id = a.get_attribute("id")
            print(f"href: {href}, id: {id}")
            self.browser.get(href)
            title = self.browser.find_element_by_id("post_title")
            self.assertEqual(title.text, a.text)

            text = Post.objects.get(id=id).text
            self.assertEqual(self.browser.find_element_by_id("content"), text)

            created_at = self.browser.find_element_by_id("created_at")
            self.assertEqual(created_at, Post.objects.get(id=id).created_at)

    def test_is_navbar_menu_exists_and_redirect_correct_url(self):
        pass

    def test_sidebar_is_exists(self):
        pass

    def test_is_category_exists_and_redirect_correct_url(self):
        # self.browser.get(f"{self.live_server_url}/post/")
        # category = self.browser.find_element_by_id("category")
        pass

    def test_tag_cloud_exists_and_redirect_correct_url(self):
        pass

    def test_footer_exists(self):
        pass
