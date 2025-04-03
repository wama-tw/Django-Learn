from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


def about(request):
    return HttpResponse("This is the about page.")


def contact(request):
    return HttpResponse("This is the contact page.")
