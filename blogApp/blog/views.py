from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category
# Create your views here.

# data = {
#     "blogs": [
#         {
#             "id": 1,
#             "title": "Web geliştirme",
#             "image": "django.png",
#             "is_active": True,
#             "is_home": False,
#             "description": "Mük bir kurs",
#         },
#         {
#             "id": 2,
#             "title": "Mobil geliştirme",
#             "image": "2.png",
#             "is_active": True,
#             "is_home": True,
#             "description": "çiçek bir kurs",
#         },
#         {
#             "id": 3,
#             "title": "Python geliştirme",
#             "image": "django.png",
#             "is_active": False,
#             "is_home": True,
#             "description": "fişek bir kurs",
#         },
#     ]
# }


def index(request):
    # static data

    # context = {
    #     "blogs": data["blogs"]
    # }

    # database data
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }

    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    # static filter method 1

    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    # static filter method 2

    # blogs = Blog.objects.all()
    # selectedBlog = [blog for blog in blogs if blog["id"] == id][0]

    # database filter method 

    selectedBlog = Blog.objects.get(slug=slug)


    return render(request, "blog/blog-details.html", {"blog": selectedBlog})


def blogs_by_category(request, slug):
    pass