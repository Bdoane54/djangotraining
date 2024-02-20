from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "recipe-smoothie",
        "title": "Smoothie Recipe",
        "image": "smoothie.jpg",
        "author": "Bryce",
        "date": date(2024, 1, 12),
        "summary": "In this blog post I will show you my best smoothie recipe",
        "content": "This is a recipe for a smoothie"
    },
    {
        "slug": "recipe-milkshake",
        "title": "Milkshake Recipe",
        "image": "milkshake.jpg",
        "author": "Bryce",
        "date": date(2024, 1, 11),
        "summary": "In this blog post I will show you my best milkshake recipe",
        "content": "This is a recipe for a milkshake"
    },
    {
        "slug": "recipe-chocolate-milk",
        "title": "Chocolate Milk Recipe",
        "image": "milk.jpg",
        "author": "Bryce",
        "date": date(2024, 1, 10),
        "summary": "In this blog post I will show you my best chocolate milk recipe",
        "content": "This is a recipe for chocolate milk"
    },
]


def get_date(post):
    return post["date"]

def landing_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })

def single_post(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
    })

