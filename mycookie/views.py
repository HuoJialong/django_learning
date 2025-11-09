from django.http.response import HttpResponse

def set_cookie(request):
    response = HttpResponse("set_cookie")
    response.set_cookie("name", "test", max_age=30)
    return response

def get_cookie(request):
    # print(request.COOKIES)
    # print(request.COOKIES.get("name"))
    return HttpResponse("get_cookie")

def delete_cookie(request):
    response = HttpResponse("delete_cookie")
    response.set_cookie("name", "test", max_age=0)
    return response