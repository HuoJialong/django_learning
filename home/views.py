from django.http.response import HttpResponse
from django.http.response import JsonResponse
import os
import json
from django.conf import settings


def index(request):
    return HttpResponse("Ok, here is home")


# Create your views here.
def index(request):
    return HttpResponse("Ok, here is home")


def index2(request):
    data = json.loads(request.body)
    # data = request.body
    print(data)
    return HttpResponse("Ok, 成功了！")


def index3(request):
    print(request.headers)
    # print(request.REMOTE_ADDR)
    return HttpResponse("Ok, here is home3")


def index4(request):
    print(request.FILES)
    return HttpResponse("Ok, here is home4")
    # return HttpResponse("Ok, here is home4")
    return HttpResponse("Ok, here is home4")


def index5(request):
    data = [
        {
            "name": "xiaoming",
            "size": "small",
        },
        {
            "name": "xiaohong",
            "size": "medium",
        }
    ]
    # data = json.dumps(data)
    # return HttpResponse("Ok, here to try jason")
    return JsonResponse(data, safe=False)


def index6(request):
    image_path = os.path.join(settings.BASE_DIR, "./home/baidu.png")
    print(image_path)
    with open(image_path, "rb") as image_file:
        # with open("./home/baidu.png", "rb") as image_file:
        img = image_file.read()
    return HttpResponse(content=img, content_type="image/png")
