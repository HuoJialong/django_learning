from django.views import View
from django.http import JsonResponse
from . import models
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
