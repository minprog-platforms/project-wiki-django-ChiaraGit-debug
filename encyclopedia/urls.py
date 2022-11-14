from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createnewpage/", views.createnewpage, name="createnewpage"),
    path("searchresults/", views.searchresults, name="searchresults"),
    path("errorpage/", views.errorpage, name="errorpage"),
    path("wiki/<str:title>", views.entrypage, name="entrypage")
]
