import os

from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    # data = {
    #     "name":"xiaohong",
    #     "age":22,
    # }
    name = "xiaoming"
    age = 20
    return render(request,"index.html", context=locals())

def index3(request):
    name = "xiaoming"
    age = 20
    book_list = [
        {"id": 1, "name": "红楼梦", "price": 300.01},
        {"id": 2, "name": "黑楼梦", "price": 400.0},
        {"id": 3, "name": "大楼梦", "price": 300.20},
        {"id": 4, "name": "绿楼梦", "price": 300.01},
    ]

    return render(request,"index3.html", context=locals())

def index4(request):
    title = "xiaoming"
    author = "xiaohong"
    content = '我的个人主页：<a href="http://www.baidu.com">点击查看</a>'
    now = datetime.now()
    filesize = os.path.getsize(__file__)
    city = ["南京", "上海", "杭州"]
    mobile = "12312345678"
    sex = 0
    return render(request,"index4.html", context=locals())
