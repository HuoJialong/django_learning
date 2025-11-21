from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.views import View
from student import models
# Create your views here.

class UserView(View):
    """这一段不写也可以，但最好是加"""
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)
    
    async def get(self, request):
        """在异步代码中，无法直接使用同步代码，所以会报错，SynchronousOnlyOperation"""
        # student_list = models.Student.objects.all()
        """在异步视图中，必须使用异步操作模型"""
        """aget就是get的异步方式，下面为拿到一条数据"""
        # aget = sync_to_async(models.Student.objects.get, thread_sensitive=True)
        # student = await aget(id=2)
        # print(student.name)
        # print(student.pk)
        # return JsonResponse({'msg': 'get'})
        """拿到多条数据"""
        student_objs = models.Student.objects.all()
        student_list=[]
        async for student in student_objs:
            student_list.append({
                'id': student.id,
                'name': student.name,
            })
        return JsonResponse({'student_list': student_list})

