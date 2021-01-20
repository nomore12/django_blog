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
        ## navbar id가 있는지 테스트
        # navbar에 home, archives, tags, about이 있는지 테스트
        # 아이템을 클릭하면 정확한 url로 이동하는지 테스트
        pass

    def test_sidebar_is_exists(self):
        ## side_bar id를 갖고있는 요소가 있는지 테스트

        # 자식 중에 프로필과 카테고리가 있는지 테스트

        ## 프로필
        # 프로필에 name, github_adress, post_cout, category_count, tag_count 요소가 있는지 테스트
        pass

        ## 카테고리
        # categories가 있는지 테스트
        # categories가 ul인지 테스트
        # 프로필의 category_count와 categories 자식들의 child_category 수가 동일한지 테스트
        # 카테고리를 클릭하면 페이지가 잘 이동하는지 테스트
        pass

    def test_is_category_exists_and_redirect_correct_url(self):
        # self.browser.get(f"{self.live_server_url}/post/")
        # category = self.browser.find_element_by_id("category")
        pass

    def test_tag_cloud_exists_and_redirect_correct_url(self):
        pass

    def test_footer_exists(self):
        pass
