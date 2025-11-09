from django.shortcuts import render

# Create your views here.
def index6(request):
    num1 = 100.78
    num2 = 200.0
    num3 = 300.784
    return render(request, 'index6.html', locals())

def index5(request):
    return render(request, "index5.html", locals())

def index7(request):
    return render(request, "index7.html", locals())

def user(request):
    return render(request, "user.html", locals())
def home(request):
    return render(request, "home.html", locals())

def get_img(request):
    return render(request, "get_img.html", locals())


