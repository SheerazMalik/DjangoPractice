from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Your at Pakistani and coding Home page")

    return render(request, "index.html" )

def about(request):
    return HttpResponse("Hello, Your at Pakistani and coding about page")

def contact(request):
    return HttpResponse("Hello, Your at Pakistani and coding contact page")