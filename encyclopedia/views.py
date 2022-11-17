# source of inspiration for this code:

from django.shortcuts import render
from django import forms
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def html_to_markdown(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def createnewpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/createnewpage.html", {"entries": util.list_entries()})

    title = request.POST['givetitle']
    text = request.POST['givetext']
    error = util.get_entry(title)
    if error != None:
        return render(request, "encyclopedia/errornewpage.html", {
            "entries": util.list_entries(),
        })
    else:
        util.save_entry(title, text)
        text_convert = html_to_markdown(title)
        return render(request, "encyclopedia/createnewpage.html", {
            "entries": util.list_entries(),
            "title": title,
            "content": text_convert,
        })

def errornewpage(request):
    return render(request, "encyclopedia/errornewpage.html", {
        "entries": util.list_entries()
    })

def searchresults(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        text_convert = html_to_markdown(entry_search)
        if text_convert != None:
            return render(request, "encyclopedia/entrypage.html", {
                "entries": util.list_entries(),
                "title": entry_search,
                "content": text_convert
            })
        else:
            allEntries = util.list_entries()
            recommendations = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendations.append(entry)
                # else:
                #     return render(request, "encyclopedia/errorsearchpage.html", {
                #         "entries": util.list_entries()
                #     })
            return render(request, "encyclopedia/searchresults.html", {
                "entries": util.list_entries(),
                "recommendations": recommendations
            })

def errorsearchpage(request):
    return render(request, "encyclopedia/errorsearchpage.html", {
        "entries": util.list_entries()
    })

def entrypage(request, title):
    text_convert = html_to_markdown(title)
    if text_convert == None:
        return render(request, "encyclopedia/errorsearchpage.html", {
            "entries": util.list_entries()
        })
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "entries": util.list_entries(),
            "get_entry": util.get_entry(title),
            "title": title,
            "content": text_convert
        })
