from django.shortcuts import render
from django.views import View
from . import models
from django.http import JsonResponse
# Create your views here.

class StudentView(View):
    def get(self, request):
        """添加数据操作"""
        #  方式1:先添加主模型数据student，再添加外键模型数据
        student = models.Student.objects.create(
            name="小白",
            age=18,
            sex=True,
        )

        models.StudentProfile.objects.create(
            # student=student,  # 通过指定对象的方式，自动绑定外键。
            student_id=student.pk,  #与上面依据等效
            # 实际上等效于student.id=student.id
            description="这是我的个性签名",
            address="学生小白的家庭住址",
            mobile="12312344679",
        )

        return JsonResponse({})