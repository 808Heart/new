from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
def index(request):
    data = {"header": "Передача параметров в шаблон Django", "message": "Загружен шаблон templates/firstapp/index_app1.html"}
    return render(request, "web/index_app1.html", context=data)
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")