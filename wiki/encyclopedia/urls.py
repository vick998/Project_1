from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("entry/", views.entry, name='entry'),
    path("newentry/", views.newentry, name='newentry')
    ]
