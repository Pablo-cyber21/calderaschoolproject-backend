# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # The homepage
    path("", views.index, name="index"),
]
