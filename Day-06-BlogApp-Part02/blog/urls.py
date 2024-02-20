from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.single_post, name="single-post-page") # /posts/about-me
    # path("post/<int:id_from>/<int:id_to>"),
    # http://localhost:8000/post/101/115
    # path("post/<slug:from_title>/<slug:to_title>")
    # http://localhost:8000/post/first-post/fifth-post
]