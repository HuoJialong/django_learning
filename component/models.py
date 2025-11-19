from django.db import models

# Create your models here.
class Software(models.Model):
    name = models.CharField(max_length=150, verbose_name="软件名称")
    version = models.CharField(max_length=50, verbose_name="软件版本")
    website = models.URLField(max_length=500, verbose_name="公司网站")
    picture = models.ImageField(upload_to="software/%Y/%m/%d/", verbose_name="缩略图")
    downloads = models.FileField(upload_to="attr/%Y/%m/%d/", verbose_name="下载地址")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_software'
        verbose_name = "应用管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}.{self.version}"

