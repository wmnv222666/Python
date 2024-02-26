from django.shortcuts import redirect, render
from project1 import models
# Create your views here.
def depart_list(request):
    """Department"""

    queryset = models.Department.objects.all()
    return render(request, "depart_list.html", {"queryset": queryset})


# def depart_add(request):
#     """add department"""
#     if request.method == "GET":
#         return render(request, "depart_add.html")

#     # get the data from POST sumbmit（title is null）
#     title = request.POST.get("title")

#     # keep to database
#     models.Department.objects.create(title=title)

#     # back to list page
#     return redirect("/depart/list/")


# def depart_delete(request):
#     """Deleter"""
#     # get ID http://127.0.0.1:8000/depart/delete/?nid=1
#     nid = request.GET.get("nid")

#     # delete
#     models.Department.objects.filter(id=nid).delete()

#     #back
#     return redirect("/depart/list/")


# def depart_edit(request, nid):
#     """edit"""
#     if request.method == "GET":
#         # nid，get  [obj,]
#         row_object = models.Department.objects.filter(id=nid).first()
#         return render(request, "depart_edit.html", {"row_object": row_object})

#     # 
#     title = request.POST.get("title")

#     # throut ID to find 
#     # models.Department.objects.filter(id=nid).update(title=title,其他=123)
#     models.Department.objects.filter(id=nid).update(title=title)

#     # 
#     return redirect("/depart/list/")


# def user_list(request):
#     """Use admition"""

#     # get all user list [obj,obj,obj]
#     queryset = models.UserInfo.objects.all()
#     """
#     # 
#     for obj in queryset:
#         print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(), obj.depart_id, obj.depart.title)
#         # print(obj.name, obj.depart_id)
#         # obj.depart_id  # 
#         # obj.depart.title  # 
#     """
#     return render(request, "user_list.html", {"queryset": queryset})


# def user_add(request):

#     if request.method == "GET":
#         context = {
#             "gender_choices": models.UserInfo.gender_choices,
#             "depart_list": models.Department.objects.all(),
#         }
#         return render(request, "user_add.html", context)

#     user = request.POST.get("user")
#     pwd = request.POST.get("pwd")
#     age = request.POST.get("age")
#     account = request.POST.get("ac")
#     ctime = request.POST.get("ctime")
#     gender = request.POST.get("gd")
#     depart_id = request.POST.get("dp")

#     # add to database
#     models.UserInfo.objects.create(
#         name=user,
#         password=pwd,
#         age=age,
#         account=account,
#         create_time=ctime,
#         gender=gender,
#         depart_id=depart_id,
#     )

#     return redirect("/user/list/")


# # ################################# ModelForm  #################################
# from django import forms


# class UserModelForm(forms.ModelForm):
#     name = forms.CharField(min_length=3, label="User")

#     class Meta:
#         model = models.UserInfo
#         fields = [
#             "name",
#             "password",
#             "age",
#             "account",
#             "create_time",
#             "gender",
#             "depart",
#         ]
#         # widgets = {
#         #     "name": forms.TextInput(attrs={"class": "form-control"}),
#         #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
#         #     "age": forms.TextInput(attrs={"class": "form-control"}),
#         # }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # class="form-control"
#         for name, field in self.fields.items():
#             # if name == "password":
#             #     continue
#             field.widget.attrs = {"class": "form-control", "placeholder": field.label}


# def user_model_form_add(request):
#     """add user（ModelForm）"""
#     if request.method == "GET":
#         form = UserModelForm()
#         return render(request, "user_model_form_add.html", {"form": form})

#     # user POST
#     form = UserModelForm(data=request.POST)
#     if form.is_valid():
#         # {'name': '123', 'password': '123', 'age': 11, 'account': Decimal('0'), 'create_time': datetime.datetime(2011, 11, 11, 0, 0, tzinfo=<UTC>), 'gender': 1, 'depart': <Department: IT运维部门>}
#         # print(form.cleaned_data)
#         # models.UserInfo.objects.create(..)
#         form.save()
#         return redirect("/user/list/")

#     return render(request, "user_model_form_add.html", {"form": form})
