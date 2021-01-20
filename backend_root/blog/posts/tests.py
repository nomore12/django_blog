from pathlib import Path

from django.test import TestCase
from django.http import HttpResponse

from posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self):
        self.post_01 = Post.objects.create(title="first post")
        self.post_02 = Post.objects.create(title="second post")
        self.post_03 = Post.objects.create(title="third post")
        self.post_04 = Post.objects.create(title="fourth post")
        self.post_05 = Post.objects.create(title="fifth post")
        self.post_06 = Post.objects.create(title="sixth post")

    def test_post_model_equals(self):
        self.assertEqual("first post", self.post_01.title)
        self.assertEqual("second post", self.post_02.title)

    def test_base_template_exists(self):
        with self.assertTemplateUsed("posts.base.html"):
            return HttpResponse("base.html")
