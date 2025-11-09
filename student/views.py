from django.http.response import JsonResponse
from django.views import View
# 第一步，加载模型
from . import models
import datetime
# Create your views here.
class StudentView(View):
    def get(self, request):

        """
        通过objects.all()的方法来获取数据
        """
        # 获取学生数据
        object_list = models.Student.objects.all()
        stu = object_list[0]
        print(stu.name)
        print(stu.create_time.strftime('%Y-%m-%d %H:%M:%S'))
        # 当字段声明中使用choices可选值选项后，在模型对象里面就可以使用.get_<字段名>_display()来获取当前选项的提示文本
        print(stu.status, stu.get_status_display())

        student_list = []
        for obj in object_list:
            # print(obj, type(obj))
            student_list.append(
                {
                    "id": obj.id,
                    "name": obj.name,
                    "age": obj.age,
                    "description": obj.description,

                }
            )
        # print(student_list)
        # student_list = []
        return JsonResponse({}, safe=False)
        """
        通过objects.values()来获取数据
        """
        # student_list = models.Student.objects.values("id", "name", "age")
        # return JsonResponse(list(student_list), safe=False)


    def post(self, request):
        # 添加学生数据
        data = {}
        return JsonResponse(data, status=201)

    def put(self, request):
        # 修改学生数据

        """
        这一部分为自己研究，怎么通过获取数据来修改模型中的数据，进而修改数据库中的数据
        """
        stu = models.Student.objects.get(id=1)
        print(stu.name)
        print(stu.update_time.strftime('%Y-%m-%d %H:%M:%S'))

        stu.name = "关羽"
        stu.update_time = datetime.datetime.now()
        stu.save()
        print(stu.name)
        print(stu.update_time.strftime('%Y-%m-%d %H:%M:%S'))

        data = {}
        return JsonResponse(data, status=201)

    def delete(self, request):
        data = {}
        return JsonResponse(data, status=204)
