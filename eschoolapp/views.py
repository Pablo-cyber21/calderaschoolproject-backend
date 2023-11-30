from django.shortcuts import render, HttpResponse, redirect


def index(request):
    """The homepage of e school"""
    return render(request, "eschoolapp/index.html")
