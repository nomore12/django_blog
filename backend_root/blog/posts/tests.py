from pathlib import Path

from django.test import TestCase

from posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self):
        self.post_01 = Post.objects.create(title="first post")
        self.post_02 = Post.objects.create(title="second post")

    def test_post_model_equals(self):
        self.assertEqual("first post", self.post_01.title)
        self.assertEqual("second post", self.post_02.title)
