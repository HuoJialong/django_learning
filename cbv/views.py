from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# Create your views here.
class UserView(View):
    def get(self, request):
        # 获取操作
        print("3.视图执行了")
        return HttpResponse('user_get')

    def post(self, request):
        # 添加操作
        return HttpResponse('user_post')

    def put(self, request):
        # 更新操作
        return HttpResponse('user_put')

    def delete(self, request):
        # 删除操作
        return HttpResponse('user_delete')

    def patch(self, request):
        # 更新操作
        return HttpResponse('user_patch')

class FormView(View):
    def get(self, request):
        # 接收表单
        return render(request,"form.html", locals())

    def post(self, request):
        print(request.POST)
        return HttpResponse("成功接收表单")

