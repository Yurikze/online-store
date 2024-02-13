from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"title": "Home - Main page", "content": "Online Guitar Store"}

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "About page",
        "content": "About Page",
        "text_on_page": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, ipsam.",
    }

    return render(request, "main/about.html", context)
