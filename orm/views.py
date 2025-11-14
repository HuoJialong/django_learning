from django.shortcuts import render
from django.views import View
from . import models
from django.http import JsonResponse
# Create your views here.

class StudentView(View):
    def get(self, request):
        """添加数据操作"""
        # #  目前的唯一方式：先添加主模型数据student，再添加外键模型数据
        # student = models.Student.objects.create(
        #     name="小白",
        #     age=18,
        #     sex=True,
        # )
        #
        # models.StudentProfile.objects.create(
        #     # student=student,  # 通过指定对象的方式，自动绑定外键。
        #     student_id=student.pk,  #与上面依据等效
        #     # 实际上等效于student.id=student.id
        #     description="这是我的个性签名",
        #     address="学生小白的家庭住址",
        #     mobile="12312344679",
        # )
        #
        # return JsonResponse({})

        """
        查询数据
        """
        """方式1:从主模型（主表，orm_student）查询到外键模型(附加表，orm_student_profile)"""
        # # 例：查询小明的电话号码和家庭住址
        # student = models.Student.objects.filter(name="小明").first()
        # if student:
        # profile就是在StudentProfile中定义的related_name
        #     print(student.profile.mobile)
        #     print(student.profile.address)
        # return JsonResponse({})

        """方式2:使用外键模型查询数据，以主键模型作为条件"""
        # student = models.StudentProfile.objects.filter(student__name="小白").first()
        # print(student)
        # return JsonResponse({})


        """方式3:根据外键模型(附加表，orm_student_profile)的参数查询主模型的数据（主表，orm_student）"""
        # 例：根据手机号，查询电话号码是谁的
        # student = models.StudentProfile.objects.filter(mobile="12312344679").first()
        # if student:
        #     print(student.student.name)
        # return JsonResponse({})

        """方式4:使用主键模型查询数据，以外键模型作为条件"""
        # stu = models.Student.objects.filter(profile__mobile="12312344679").first()
        # print(stu)
        # return JsonResponse({})

        """
        修改数据
        """
        # 例：修改小明的家庭住址，根据主键条件来修改外键模型数据
        # stu1 = models.Student.objects.filter(name="小明").first()
        # stu1.profile.address = "更新后的小明的家庭住址"
        # print(stu1)
        # print(stu1.profile)
        # stu1.profile.save()

        # 例：根据电话号码修改人名，根据外键模型条件修改主键数据
        # stu2 = models.StudentProfile.objects.filter(mobile="12312345679").first()
        # stu2.student.name = "更新后的名字"
        # stu2.student.save()

        # 例：通过update进行更新数据
        # 更新小红的家庭地址
        # models.StudentProfile.objects.filter(student__name="小白").update(address="更新后的小白的家庭住址")
        # models.Student.objects.filter(profile__mobile="12312345679").update(age=20)
        # return JsonResponse({})

        """
        删除操作
        """