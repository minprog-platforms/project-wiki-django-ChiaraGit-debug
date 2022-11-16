from django.shortcuts import render
from django import forms
# import entries as md
# from django import template
# from django.template.defaultfilters import stringfilter
import markdownify

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



# class NewTaskForm(forms.Form):
#     title = forms.CharField(label="Title")
#     text = forms.CharField(label="Text")

def createnewpage(request):
    # if request.method == "POST":
    #     title = request.POST['givetitle'],
    #     text = request.POST['givetext'],
    #     util.save_entry(title, text)
        return render(request, "encyclopedia/createnewpage.html", {
            "entries": util.list_entries(),
            # "form": NewTaskForm()
        })

        # form = NewTaskForm(request.POST)
        # if form.is_valid():
        #     title = form.cleaned_data["title"]
        #     return render(request, "encyclopedia/index.html", {
        #         "entries": util.list_entries()
        #     })
        # else:
        #      return render(request, "encyclopedia/createnewpagehtml", {
        #         "form": form
        #     })





def searchresults(request):
    return render(request, "encyclopedia/searchresults.html", {
        "entries": util.list_entries()
    })

def errorpage(request):
    return render(request, "encyclopedia/errorpage.html", {
        "entries": util.list_entries()
    })

def entrypage(request, title):
    return render(request, "encyclopedia/entrypage.html", {
        "entries": util.list_entries(),
        "get_entry": util.get_entry(title)
    })
