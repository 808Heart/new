from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
def index(request):
    return render(request, "index.html")
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")