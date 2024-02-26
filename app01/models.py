from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    # pub_data = models.DateField("date published")


"""
create table django2(
    id bigint auto_increment primary key,
    name varchar(32),
    password(32),
    age(int)
)

"""


class Department(models.Model):
    title = models.CharField(max_length=16)

    # #### 1.新建 ####
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")
    # UserInfo.objects.create(name="武沛齐", password="123", age=19)
    # UserInfo.objects.create(name="朱虎飞", password="666", age=29)
    # UserInfo.objects.create(name="吴阳军", password="666")

    # #### 2.删除 ####
    # UserInfo.objects.filter(id=3).delete()
    # Department.objects.all().delete()

    # #### 3.获取数据 筛选####
    # data_list = UserInfo.objects.all()
    # 3.1 获取符合条件的所有数据
    # data_list = [对象,对象,对象]  QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # data_list = [对象,]
    # data_list = UserInfo.objects.filter(id=1)
    # print(data_list)！！！！
    # 3.1 获取第一条数据【对象】
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)


    # #### 4.更新数据 ####
    # UserInfo.objects.all().update(password=999)
    # UserInfo.objects.filter(id=2).update(age=999)
    # UserInfo.objects.filter(name="朱虎飞").update(age=999)
