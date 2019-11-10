#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the hello index Oneeee.")

def index2(request):
    return HttpResponse("Hello, world. You're at the hello index Twoooo.")


def index3(request):
    return HttpResponse("Hello, world. You're at the hello index Threeee.")
