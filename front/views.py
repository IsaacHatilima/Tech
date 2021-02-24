from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return render(response, "front/home.html", {})


def about(response):
    return render(response, "front/about.html", {})


def services(response):
    return render(response, "front/services.html", {})




def contact(response):
    return render(response, "front/contact.html", {})
