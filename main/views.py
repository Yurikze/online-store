from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


# Create your views here.
def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - Main page",
        "content": "Online Guitar Store",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About page",
        "content": "About Page",
        "text_on_page": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, ipsam.",
    }

    return render(request, "main/about.html", context)
