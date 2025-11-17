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
    """1对1的虚拟外键设置，添加db_constraint=False，不影响增查删改的任何操作和语法"""
    # student = models.OneToOneField("Student", on_delete=models.CASCADE, db_constraint=False, related_name="profile")
    """"""
    # on_delete表示主键数据删除时，外键模型数据怎么处理，主要有5个常用表示
    # on_delete = models.CASCADE,株连/级联  删除主键数据，外键对应数据同步删除。但删除外键数据，不影响主键数据
    # on_delete = models.DO_NOTHING  不进行操作
    # on_delete = models.DEFERRED   删除保护，即删除主键数据时，必须确认外键数据已经删除了
    # on_delete = models.SET_NULL   设为空
    # on_delete = models.SET_DEFAULT  设为默认值
    description = models.TextField(default="", verbose_name="个性签名")
    address = models.CharField(max_length=500, verbose_name="家庭住址")
    mobile = models.CharField(max_length=15, verbose_name="紧急联系人")

    class Meta:
        db_table = "orm_student_profile"
        verbose_name = "学生详细信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"address": self.address, "mobile": self.mobile})


class Author(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(null=True, blank=True, default=None, verbose_name="性别")

    class Meta:
        db_table = "orm_author"
        verbose_name = "作者信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"name": self.name, "age": self.age, "sex": self.sex})


class Article(models.Model):
    title = models.TextField(default="", verbose_name="文章名称")
    pub_date = models.DateTimeField(null=True, verbose_name="发布时间")
    content = models.TextField(null=True, verbose_name="文章内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    author = models.ForeignKey("Author", on_delete=models.DO_NOTHING, related_name="article_list", verbose_name="作者")
    """1对多的虚拟外键设置，添加db_constraint=False，不影响增查删改的任何操作和语法"""
    # author = models.ForeignKey("Author", on_delete=models.DO_NOTHING, db_constraint=False, related_name="article_list", verbose_name="作者")
    class Meta:
        db_table = "orm_article"
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"title": self.title, "pub_date": self.pub_date,
                    "create_time": self.create_time,
                    "update_time": self.update_time})


"""多对多：老师——课程"""


class Teacher(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(null=True, blank=True, default=None, verbose_name="性别")

    class Meta:
        db_table = "orm_teacher"
        verbose_name = "老师信息"
        verbose_name_plural = verbose_name


class Course(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="课程名称")
    teacher = models.ManyToManyField("Teacher", related_name="course")

    class Meta:
        db_table = "orm_course"
        verbose_name = "课程表"
        verbose_name_plural = verbose_name


"""
自关联。（1）一对多自关联，行政区域划分；（2）多对多自关联，用户好友
"""

class Area(models.Model):
    # 一对多的自关联模型，例子为行政划分
    name = models.CharField(max_length=50, verbose_name="省市名称")
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    class Meta:
        db_table = "orm_area"
        verbose_name = "行政划分表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"id": self.id, "name": self.name})

class User(models.Model):
    # 多对多自关联模型，例子为用户之前的相互好友关系
    name = models.CharField(max_length=30, unique=True, verbose_name="用户名")
    age = models.SmallIntegerField(default=0, verbose_name="年龄")
    # 因为自关联的多对多极易形成递归寻找，因此，django默认不支持多对多的反向查询，
    # 但是可以通过设置symmetrical=True来设置为支持
    friends = models.ManyToManyField("self", symmetrical=True)

    class Meta:
        db_table = "orm_user"
        verbose_name = "好友关注表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str({"name": self.name, "age": self.age})
