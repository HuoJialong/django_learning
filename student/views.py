from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from django.views import View
import json
from django.db import IntegrityError
# 第一步，加载模型
from . import models
import datetime
from faker import Faker
import random


# Create your views here.
class StudentView(View):
    def get(self, request):

        """
        通过objects.all()的方法来获取数据
        """
        # 获取学生数据
        # object_list = models.Student.objects.all()
        # stu = object_list[0]
        # print(stu.name)
        # print(stu.create_time.strftime('%Y-%m-%d %H:%M:%S'))
        # # 当字段声明中使用choices可选值选项后，在模型对象里面就可以使用.get_<字段名>_display()来获取当前选项的提示文本
        # print(stu.status, stu.get_status_display())
        #
        # student_list = []
        # for obj in object_list:
        #     # print(obj, type(obj))
        #     student_list.append(
        #         {
        #             "id": obj.id,
        #             "name": obj.name,
        #             "age": obj.age,
        #             "description": obj.description,
        #
        #         }
        #     )
        # # print(student_list)
        # # student_list = []
        # return JsonResponse({}, safe=False)
        """
        通过objects.values()来获取数据
        """
        # student_list = models.Student.objects.values("id", "name", "age")
        # return JsonResponse(list(student_list), safe=False)

        """
        过滤操作
        """
    # #     1.相等运算符 exact或者=
    #     stu1 = models.Student.objects.filter(id=3).first()
    #     print(stu1,type(stu1))
    #     stu2 = models.Student.objects.filter(id__exact=3).first()
    #     print(stu2, type(stu2))
    #     return JsonResponse({})

    # # 2.模糊查询contains，相当于sql中的like
    # # 模型类.objects.filter(字段名__contains="值")
    # # 查询名字中包含“华”字的同学
    #     stu3=models.Student.objects.filter(name__contains="华").values()
    #     print(stu3, type(stu3))
    #     return JsonResponse(list(stu3), safe=False)

    # # 3.查询以固定值开头的数据
    # # 查询姓李的学生
    #     stu4 = models.Student.objects.filter(name__startswith="李").values()
    #     print(stu4)
    #     return JsonResponse(list(stu4),safe=False)

        # 4.查询以固定值结尾的数据
        # 查询名字最后一个字是"梅"的学生
        stu5 = models.Student.objects.filter(name__endswith="梅").all()
        print(stu5)
        return  JsonResponse({})





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
        #
        stu1 = models.Student(name="老大", age=10, sex="M", classmate="201", mobile="12312345678", description="老大",
                              status=1)
        # stu2 = models.Student(name="老二",age=9,sex="F",classmate="301",mobile="12314345678", description="老二",status=2)
        # stu3 = models.Student(name="老三",age=8,sex="F",classmate="401",mobile="12313345678", description="老三",status=0)
        # ret = models.Student.objects.bulk_create([stu1,stu2,stu3])
        # print(ret)

        # print(request.body)
        # return JsonResponse({"succeed!": len(ret)}, status=201, safe=False)
        #     使用faker来生成虚拟数据，存储到student表中
        faker = Faker('zh_CN')
        for num in range(100):
            stu1 = models.Student(
                id=num + 1,
                name=faker.name(),
                age=random.randint(6, 12),
                sex=random.choice(["M", "F"]),
                classmate=random.choice(["201", "202", "301", "302", "401"]),
                mobile=str(faker.phone_number()),
                description=faker.sentence(),
                status=random.choice([0, 1, 2]))
            stu1.save()
            # student = models.Student(
            #     "name" = faker.name(),
            # )
        return JsonResponse({})

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

        # data = {}
        # return JsonResponse(data, status=201)

        """
        使用save（）保存当前数据模型，并同步到数据库
        使用save（）修改模型数据可以修改一条或多条，只需最后使用save（）进行保存即可
        """
        # stu2 = models.Student.objects.get(id=1)
        # faker = Faker('zh_CN')
        # stu2.name = faker.name()
        # stu2.save()
        # return JsonResponse({})

        """
        使用update更新符合条件的模型一条或几条数据
        例如将id=5，6的两名同学班级改为101
        """
        # stu3 = models.Student.objects.filter(id__in=[5,  6]).all()
        # print(stu3)
        models.Student.objects.filter(id__in=[5,6]).update(classmate="101")
        return JsonResponse({})

    def delete(self, request):
        """
        模型对象.delete()
        """
        # try:
        #     stu4 = models.Student.objects.get(id=120)
        #     stu4.delete()
        # except models.Student.DoesNotExist:
        #     print("模型对象不存在")
        #     pass
        # return JsonResponse({}, status=204)

        """
        模型类.objects.delete() #删除全表数据，慎用！
        模型类.objects.filter(条件).delete()  #删除表中满足条件的一条或多条数据
        """
#         删除id>95的数据
        models.Student.objects.filter(id__gte=95).delete()
        return JsonResponse({})
