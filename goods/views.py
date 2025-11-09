from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request)
    data = "Hello World"
    return HttpResponse(data)

def hello_world(request):
    print(request)
    return HttpResponse("I have no idea")