from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf.urls import handler404

from posts.models import Post


# class PostListView(ListView):
#     model = Post
#     template_name = "posts.post_list.html"


def PostListView(request):
    if request.method != "GET":
        return handler404()
    return render(
        request,
        "posts/post_list.html",
        context={"object_list": Post.objects.all()},
    )


def PostDetailView(request, pk):
    if request.method != "GET":
        return handler404()
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", context={"object": post})
