from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf.urls import handler404

from posts.models import Post


def PostListView(request):
    if request.method != "GET":
        return handler404()
    context = sorted(
        [
            {"posts": post, "desc": post.text[0:300]}
            for post in Post.objects.all()
        ],
        key=lambda e: e["posts"].pk,
        reverse=True,
    )
    return render(
        request,
        "posts/post_list.html",
        context={"context": context},
    )


def PostDetailView(request, slug):
    if request.method != "GET":
        return handler404()
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_detail.html", context={"object": post})
