from django.db import models

# Create your models here.
"""
此处是对应的sql语句

create table if not exists 'student'(
    name varchar(15),
    key name(name),
    age smallint,
    sex tinyint default 1,
    class  varchar(50) default "",
    mobile varchar(20) default "",
    constraint mobile unique (mobile),
    description text，
    status int default 1
    )
"""


class BaseModel(models.Model):
    # auto_now_add 设置当前字段会在新建数据时，把当前时间戳作为默认值保存到数据库中
    create_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    # auto_now 设置当前字段会在修改数据时，把当前时间戳作为默认值保存到数据库中
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")

    class Meta:
        #  设置当前类为抽象模型，表示当前模式并不是一个真正的表，django就不会跟踪识别这个模型了
        abstract = True


class Student(BaseModel):
    STATUS = ((0, "未入学"), (1, "在校"), (2, "已毕业"),)  # 通过.get_<字段名>_display()可以拿到提示文本
    GENDER_CHOICES = (("M", "男"), ("F", "女"))
    # django模型中不需要自己声明主键，模型会自动生成主键id，将来直接通过模型对象.id或者模型对象.pk进行调用
    name = models.CharField(max_length=15, db_index=True, verbose_name="姓名")
    age = models.IntegerField(default=0, verbose_name="年龄")
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES, default=True, verbose_name="性别")
    classmate = models.CharField(max_length=50, db_column="class", default="", db_index=True, verbose_name="班级")
    mobile = models.CharField(max_length=20, unique=True, verbose_name="手机号")
    description = models.TextField(blank=True, null=True, verbose_name="个性签名")
    status = models.IntegerField(choices=STATUS, default=1, null=True, verbose_name="毕业情况")


    class Meta:
        db_table = "student"
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 当使用print打印django模型对象时的输出内容
        return self.name
