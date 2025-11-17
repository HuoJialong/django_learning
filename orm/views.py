from tkinter.font import names

from django.shortcuts import render
from django.views import View
from . import models
from django.http import JsonResponse
import datetime

from .models import Course


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
        return JsonResponse({})


class ArticleView(View):
    def get(self, request):
        """
        添加数据
        """
        """1.从0开始添加数据"""
        # author = models.Author.objects.create(
        #     name="小明",
        #     age=19,
        #     sex=True,
        # )
        # article_list = [
        #     models.Article(title="文章1", content="这是文章1", pub_date="2024-01-01 10:00:00",author=author),
        #     models.Article(title="文章2", content="这是文章2", pub_date="2025-07-09 11:00:00", author_id=author.id)
        # ]
        # models.Article.objects.bulk_create(article_list)

        """2.给主模型中已有的作者添加数据"""
        # author1 = models.Author.objects.filter(name="小明").first()
        # if author1:
        #     article_list1 = [
        #         models.Article(title="文章3", content="这是文章3", pub_date="2020-09-01 10:00:00",author=author1),
        #         models.Article(title="文章4", content="这是文章4", pub_date="2020-06-09 11:00:00", author_id=author1.id)
        #     ]
        #     models.Article.objects.bulk_create(article_list1)

        # return JsonResponse({})

        """
        查询数据
        """
        # 查询小明发表的文章
        # 方法1
        # author = models.Author.objects.filter(name="小明").first()
        # if author:
        #     print(author)
        #     print(author.article_list.all())
        # return JsonResponse({})
        #         方法2:主键作为条件进行查询
        #         article = models.Article.objects.filter(author__name="小明").all()
        #         print(article)
        #         return JsonResponse({})
        #        例：查询文章标题的作者
        #         author = models.Author.objects.filter(article_list__title="文章2").first()
        #         print(author.name)
        #         return JsonResponse({})

        """
        修改数据
        """
        """将作者为小明的文章的pub_date都改为2025-09-11 10:00:00"""

        # article = models.Article.objects.filter(author__name="小明")
        # for item in article:
        #     item.update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     item.save()
        # # print(article, type(article))
        # # article["pub_date"] = "2025-09-11 10:00:00"
        #
        # return JsonResponse({})


class TeacherView(View):
    def get(self, request):
        """
        添加数据,通过.add绑定关系
        """
        # teacher = models.Teacher.objects.create(
        #     name="小明",
        #     age=32,
        #     sex=False,
        # )
        # course = models.Course.objects.create(
        #     name="数学课"
        # )
        # # 绑定上面创造的两个对象之间的关系
        # teacher.course.add(course)
        #
        # teacher1 = models.Teacher.objects.filter(name="小明").first()
        # course1 = models.Course.objects.create(name="英语课")
        # course2 = models.Course.objects.create(name="语文课")
        # teacher1.course.add(course1, course2)
        #
        # return JsonResponse({})

        """
        查询数据
        """
        # 查询名为小明的老师的所有课程
        # 先查询一个模型，再查询另外一个模型
        # teachers = models.Teacher.objects.filter(name="小明").first()
        # print(teachers.course.values())

        # 主模型作为条件来查询外键模型的数据
        # course_list = models.Course.objects.filter(teacher__name="小明").values()
        # for course in course_list:
        #     print(course, type(course), course["name"])
        # return JsonResponse({})

        """
        更新数据
        """
#       将名为小明的老师的课程后面加上（专课）
#         teacher = models.Teacher.objects.filter(name="小明").first()
#         print(teacher)
#         for course in teacher.course.all():
#             course.name = course.name + "(专课)"
#             course.save()

        from django.db.models import F, Value
        from django.db.models.functions import Concat
        # # 下面这种方式只能用于整型
        models.Course.objects.filter(teacher__name="小明").update(name=Concat(F("name"), Value("新增"))) #这是可以的
        # models.Teacher.objects.update(age=F("age")+1) # 这是可以的

#
        # return JsonResponse({})
        """
        删除之后，mysql会自动删除绑定关系
        """
        models.Teacher.objects.filter(name="小红").delete()

        """
        解绑关系
        """
        teacher = models.Teacher.objects.filter(name="小明").first()
        course = models.Course.objects.filter(name="数学课").first()
        teacher.course.remove(course)
        return JsonResponse({})

class AreaView(View):
    def get(self, request):
        # 注意创建
        # area1 = models.Area.objects.create(name="江苏省")
        # area2 = models.Area.objects.create(name="河北省")
        #
        # area3 = models.Area.objects.create(name="南京市", parent=area1)
        # area4 = models.Area.objects.create(name="苏州市", parent=area1)
        # area5 = models.Area.objects.create(name="常州市", parent=area1)
        #
        # area6 = models.Area.objects.create(name="鼓楼区", parent=area3)
        # area7 = models.Area.objects.create(name="玄武区", parent=area3)
        # area8 = models.Area.objects.create(name="秦淮区", parent=area3)
        # 批量创建
        # area9 = models.Area.objects.create(name="浙江省")
        # area_list = [
        #     models.Area(name="杭州市"),
        #     models.Area(name="湖州市"),
        #              ]
        # # bulk属性只有在一对多的时候才存在
        # area9.children.add(*area_list,bulk=False)
        # return JsonResponse({})
        """
        查询数据
        """
#       查询河南省的所有城市
        province = models.Area.objects.filter(name="江苏省").first()
        print(province.children.all())

        # 查询秦淮区属于哪个城市
        city = models.Area.objects.filter(children__name="秦淮区").first()
        print(city.name)
        return JsonResponse({})
