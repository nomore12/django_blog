from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView, name="list"),
    path("<slug:slug>", views.PostDetailView, name="detail"),
]