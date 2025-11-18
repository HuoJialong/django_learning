from django.views import View
from psutil import users

from . import models
from django.http import JsonResponse
# Create your views here.

class UserView(View):
    def get(self, request):
        users = models.User.objects.all()
        print(users)
        print(models.User.objects.filter(age__gte=18).all())

        """当需要给模型扩展一些属性或者数据操作方法时，可以使用自定义模型管理器或者代理模型"""
        print(models.User.objects.get_user())
        """也可以使用模型类方法来实现，只不过代码风格会有所不同"""
        print(models.User.get_user_list())

        """使用模型代理器的写法"""
        print(models.Female.all())
        print(models.Male.all())
        return JsonResponse({})
