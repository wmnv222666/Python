from django.http import HttpResponse
from django.shortcuts import render,redirect
from app01.models import Department,UserInfo#导入数据库的表


def index(request):
    return HttpResponse("Hello, world. This is your Django app!")


# def user_list(request):
#     return  HttpResponse("hello")


def user_list(request):
    return render(request,"user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name ="Alex"
    roles = ["manager","CEO"]
    user_info ={"name":"alex","age":18,"sex":"mele"}
    data = [
        {"name": "alex", "age": 18, "sex": "mele"},
        {"name": "alex1", "age": 23, "sex": "mele"},
    ]

    return render(request, "tpl.html", {'n1': name, 'n2': roles, 'n3': user_info,'n4':data})


import requests


# 如果是谷歌地图的网页返回的是 HTML 页面，而不是 JSON 数据。你应该使用 res.text
def news(request):
    res = requests.get("https://www.google.com/maps?authuser=0")
    html_content = res.text
    return render(request, "news.html", {'html_content': html_content})


def news(request):
    import requests
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    json_data = res.json()
    print(json_data)
    return render(request, "news.html", {'json_data': json_data})

def something(request):
    # 1get or post
    # print(request.method)

    # 2.url  http://127.0.0.1:8000/something/n1=123&b2=999
    # print(request.GET)
    # print(request.POST)

    # return HttpResponse("aaa")
    # return render(request,'something.html',{"title":"come on"})

    # 响应到页面
    return redirect('https://www.google.com/')


      # 操作这个数据库
        # from app01.models import Department, UserInfo  # 导入数据库的表


# 用户登录

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  # 处理 POST 请求  ！！！ 也可以省略else 因为不是
        # print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 进行校验
        if username == 'root' and password == '123':#校验密码应该和数据库进行校验
            # return redirect('https://www.google.com/')发送成功跳转到一个
            return HttpResponse('Successfully')
        else:#这里也可以省略else
            return render(request, 'login.html',{"error_msg":"login failt"})#登录失败返回当前页
            # return HttpResponse('Error')


def orm(request):
    #  Department.objects.create(title:"education")
    #  Department.objects.create(title:"admintion")
    # UserInfo.objects.create(name="alex", password="alex", age=18)
    # UserInfo.objects.create(name="alex1", password="alex1", age=28)
    # UserInfo.objects.filter(id=3).delete()
    # UserInfo.objects.filter(id=4).delete()
    # UserInfo.objects.filter(id=5).delete()
    # row_obj = UserInfo.objects.filter(id=6).first()
    # print(row_obj)  # UserInfo object (6)
    # #### 4.更新数据 ####
    # UserInfo.objects.all().update(password=999)
    # UserInfo.objects.filter(id=2).update(age=999)
    # UserInfo.objects.filter(name="朱虎飞").update(age=999)

    return HttpResponse("successfully")


def info_list(request):
    # 1.get all info
    data_list = UserInfo.objects.all()
    print(data_list)
    return render(request, "info_list.html", {"data_list": data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request, "info_add.html")
    # 获取数据提交的
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 提交到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)
    # 添加成功跳转到自己的网站
    # return HttpResponse('succ')
    return redirect("http://127.0.0.1:8000/info/list/")

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    # return HttpResponse('succ')
    return redirect("http://127.0.0.1:8000/info/list/")
