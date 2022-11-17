from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createnewpage/", views.createnewpage, name="createnewpage"),
    path("searchresults/", views.searchresults, name="searchresults"),
    path("errorsearchpage/", views.errorsearchpage, name="errorsearchpage"),
    path("wiki/<str:title>", views.entrypage, name="entrypage"),
    path("errornewpage/", views.errornewpage, name="errornewpage"),
    ]
