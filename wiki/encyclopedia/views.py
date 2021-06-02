from django.shortcuts import render
from django import forms
from django.core.exceptions import ValidationError
from django.http import QueryDict
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.files.base import ContentFile
from . import util

def index(request):
	return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
	if title.lower() in util.lowercase():
		return render(request, "encyclopedia/title.html", {
			"title": title, 
			"titledetail": util.get_entry(title)
			})
	else:
		return render(request, "encyclopedia/error.html", {
			"title": title
			})

def search(request):
	if request.method == "GET":
		title1 = request.GET.get("q")
		if title1.lower() in util.lowercase():
			return render(request, "encyclopedia/title.html", {
			"title": util.nametitle(title1), 
			"titledetail": util.get_entry(title1)
			})
		else:
			return render(request, "encyclopedia/search.html", {
			"titl": title1.lower(),
			"titles": util.lowercase()
			})

def entry(request):
	if request.method == "GET":
		title1 = request.GET.get("q1")
		if title1 in util.lowercase():
			return render(request, "encyclopedia/title.html", {
			"title": util.nametitle(title1), 
			"titledetail": util.get_entry(title1)
			})


def DataCheck(value):
		titles = util.lowercase()
		if value in titles:
			raise ValidationError("Already exists")

class NewEntryForm(forms.Form):
	title = forms.CharField(label="title", validators=[DataCheck]);
	descr = forms.CharField(label="descr");


def newentry(request):
	if request.method == "POST":
		newent = NewEntryForm(request.POST)
		title1 = request.POST.get("title")
		descr1 = request.POST.get("descr")
		if newent.is_valid():
			util.save_entry(title1, descr1)
			return render(request, "encyclopedia/title.html", {
			"title": request.POST.get("title"), 
			"titledetail": util.get_entry(request.POST.get("title"))
			})
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "encyclopedia/error1.html", {
				"title" : request.POST.get("title")
				})
	return render(request,"encyclopedia/newentry.html",{
		"newent": NewEntryForm()
		})
