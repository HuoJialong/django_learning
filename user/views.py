from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def info(request, id):
    return HttpResponse(f"id={id}的用户信息")

def inbuild_reverse(request, num):
    return HttpResponse(f"num={num}")

def inbuild_reverse2(request, content):
    return HttpResponse(f"content={content}")