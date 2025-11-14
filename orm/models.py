from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(null=True, blank=True, default=None, verbose_name="性别")

    class Meta:
        db_table = "orm_student"
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"id": self.pk, "name": self.name, "age": self.age, "sex": self.sex})

class StudentProfile(models.Model):
    # 从主键模型查询外键模型用.profile
    # 从外键模型查询主键模型用.student
    student = models.OneToOneField("Student", on_delete=models.CASCADE, related_name="profile")
    # CASCADE: 株连/级联
    description = models.TextField(default="", verbose_name="个性签名")
    address = models.CharField(max_length=500, verbose_name="家庭住址")
    mobile = models.CharField(max_length=15, verbose_name="紧急联系人")

    class Meta:
        db_table = "orm_student_profile"
        verbose_name = "学生详细信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"address": self.address, "mobile": self.mobile})
