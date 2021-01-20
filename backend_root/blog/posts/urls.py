from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView, name="list"),
    path("<int:pk>", views.PostDetailView, name="detail"),
]