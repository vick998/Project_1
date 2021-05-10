from django.shortcuts import render
from django import forms
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


def newentry(request):
	if request.method == "POST":
		title = request.POST["q2"]
		text = request.POST["t1"]
		titles = util.lowercase()
		if title in titles:
			except(KeyError)
			return render(request, "encyclopedia/error1.html", {
				"title" : title
				})
			# return HttpResponseRedirect('/newentry/error1.html')
		else:
			util.save_entry(title, text)
			return render(request, "encyclopedia/title.html", {
			"title": title, 
			"titledetail": util.get_entry(title)
			})
			return HttpResponseRedirect("/title")
	return render(request,"encyclopedia/newentry.html")
