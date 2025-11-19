from django.db.models.expressions import result
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from . import models
from student.models import Student
from django.core.paginator import Paginator
# Create your views here.

class SoftwareView(View):
    def post(self,request):
        # 接收来自客户端的数据
        name = request.POST.get("name")
        version = request.POST.get("version")
        website = request.POST.get("website")
        picture = request.FILES.get("picture")
        downloads = request.FILES.get("downloads")
        software = models.Software.objects.create(
            name=name,
            version=version,
            website=website,
            picture=picture,
            downloads=downloads
        )
        # print(request.META)
        return JsonResponse({
            "id": software.id,
            "name": software.name,
            "version": software.version,
            "website": software.website,
            "picture": f"//{request.META.get('HTTP_HOST')}{software.picture.url}",
            "downloads": f"//{request.headers.get('host')}{software.downloads.url}",
            "create_time": software.create_time,
            "update_time": software.update_time,
        })

    def delete(self,request):
        software = models.Software.objects.filter(id=request.GET.get("id")).first()
        print(software.picture.path)
        software.delete()
        return JsonResponse({})

class StudentView(View):
    def get(self,request):
        """数据分页"""
        """提供了数据对象列表及单页数据，并创建了分页器对象"""
        stu1 = Student.objects.all()
        paginator = Paginator(stu1, 10)
        # print(stu1)
        print(paginator.num_pages,
              paginator.count,
              paginator.page_range)
        """基于分页器对象，创业分页对象"""
        # 接收客户端的页面，页面一般都是查询字符串，或者路径参数
        currentPage = request.GET.get("page", 1)  # 这里的1是默认值
        page = paginator.get_page(currentPage)
        # 当前页码的要展示的数据
        print(page.object_list)
        # 当前页码
        print(page.number)
        # 当前页码的父级分页器对象
        print(page.paginator)
        # output = []
        # for item in page.object_list:
        #     output.append(item)
        return render(request, "component.html", locals())
