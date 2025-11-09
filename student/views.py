from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.views import View
import json
from django.db import IntegrityError
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

        # 1.接收客户端发来的数据
        para = json.loads(request.body)

        # 2.参数校验和格式转换

        # 3.基于模型的save()方法就可以完成模型对象的更新或者添加
        # try:
        #     student = models.Student(
        #         name=para["name"],
        #         age=para["age"],
        #         sex=para["sex"],
        #         classmate=para["classmate"],
        #         mobile=para["mobile"],
        #         description=para["description"],
        #         status=para["status"])
        #     student.save()
        #     return HttpResponse("添加成功！")
        # except IntegrityError:
        #     return HttpResponse(f"添加失败，错误信息：{IntegrityError}")


        # 模型的.objects.create可以用以创建新对象
        # student = models.Student.objects.create(
        #     name=para["name"],
        #     age=para["age"],
        #     sex=para["sex"],
        #     classmate=para["classmate"],
        #     mobile=para["mobile"],
        #     description=para["description"],
        #     status=para["status"],
        # )

        # 4.返回结果
        # data = {
        #     "id": student.pk,
        #     "name": student.name,
        #     "age": student.age
        # }

        stu1 = models.Student(name="老大",age=10,sex="M",classmate="201",mobile="12312345678", description="老大",status=1)
        stu2 = models.Student(name="老二",age=9,sex="F",classmate="301",mobile="12314345678", description="老二",status=2)
        stu3 = models.Student(name="老三",age=8,sex="F",classmate="401",mobile="12313345678", description="老三",status=0)
        ret = models.Student.objects.bulk_create([stu1,stu2,stu3])
        print(ret)

        # print(request.body)
        return JsonResponse({"succeed!": len(ret)}, status=201, safe=False)

    def put(self, request):
        # 修改学生数据

        """
        这一部分为自己研究，怎么通过获取数据来修改模型中的数据，进而修改数据库中的数据
        """
        # stu = models.Student.objects.get(id=1)
        # print(stu.name)
        # print(stu.update_time.strftime('%Y-%m-%d %H:%M:%S'))
        #
        # stu.name = "关羽"
        # stu.update_time = datetime.datetime.now()
        # stu.save()
        # print(stu.name)
        # print(stu.update_time.strftime('%Y-%m-%d %H:%M:%S'))

        data = {}
        return JsonResponse(data, status=201)

    def delete(self, request):
        data = {}
        return JsonResponse(data, status=204)
