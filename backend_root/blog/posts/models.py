from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    """
    Post 모델
    """

    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(
        "SLUG",
        unique=True,
        allow_unicode=True,
        max_length=100,
        default="default",
    )
    text = models.TextField(blank=False, default="default")
    tag = models.ManyToManyField("Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Tag(models.Model):
    name = models.CharField(max_length=40)
