from django.http import HttpResponse

def set_session(response):
    response.session["user_id"] = 1
    response.session["user_name"] = "user"
    return HttpResponse("set_session")

def get_session(request):
    print(dict(request.session.items()))
    return HttpResponse("get_session")
    return HttpResponse("get_session")

def del_session(response):
    return HttpResponse("del_session")
