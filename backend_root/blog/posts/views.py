from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
