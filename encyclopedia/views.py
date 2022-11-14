from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def createnewpage(request):
    return render(request, "encyclopedia/createnewpage.html")

def searchresults(request):
    return render(request, "encyclopedia/searchresults.html")

def errorpage(request):
    return render(request, "encyclopedia/errorpage.html")

def entrypage(request):
    return render(request, "encyclopedia/title.html")
