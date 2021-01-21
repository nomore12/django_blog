from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf.urls import handler404

from posts.models import Post


# class PostListView(ListView):
#     model = Post
#     template_name = "posts.post_list.html"


def PostListView(request):
    import pprint

    # pprint.pprint(dir(request))
    # print("post view")
    # print(f"path: {request.path}")
    # print(f"urlconf: {request.urlconf()}")
    # print(f"read: {request.read()}")
    if request.method != "GET":
        return handler404()
    return render(
        request,
        "posts/post_list.html",
        context={"object_list": Post.objects.all()},
    )


def PostDetailView(request, slug):
    if request.method != "GET":
        return handler404()
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_detail.html", context={"object": post})
