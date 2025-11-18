from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.base import Manager

# Create your models here.

"""这里定义了自己的方法"""
class UserManager(Manager):
    def get_user(self, **kwargs):
        return self.filter(age__gte=18).all()


class User(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(null=True, blank=True, default=None, verbose_name="性别")
    # 这里进行了实例化，这样写会使得代码风格保持一致
    objects = UserManager()

    class Meta:
        db_table = "tb_user"
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 刚才的自定义模型管理器，也可以使用模型类方法来实现，只不过这样的话，代码风格和原来会有区别
    @classmethod
    def get_user_list(cls):
        return cls.objects.filter(age__gte=18).all()


class Female(User):

    class Meta:
        proxy = True   # 声明当前为代理模型

    @classmethod
    def all(cls):
        return cls.objects.filter(sex=False).all()

class Male(User):

    class Meta:
        proxy = True   # 声明当前为代理模型

    @classmethod
    def all(cls):
        return cls.objects.filter(sex=True).all()
