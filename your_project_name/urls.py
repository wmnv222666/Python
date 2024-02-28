from django.contrib import admin
from django.urls import path
from app01 import views as app01_views
from project1 import views as project1_views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # www.xxx.com/index/ 也就是说一旦启动就会到app01中的view中找到admin.site.urls这个函数
    path("index/", app01_views.index),
    path("user/list", app01_views.user_list),
    path("user/add", app01_views.user_add),
    path("tpl", app01_views.tpl),
    path("news", app01_views.news),
    path("something/", app01_views.something),
    path("login/", app01_views.login),
    path("orm/", app01_views.orm),
    path("info/list/", app01_views.info_list),
    path("info/add/", app01_views.info_add),
    path("info/delete/", app01_views.info_delete),
    path("depart/list/", project1_views.depart_list),
    path("depart/add/", project1_views.depart_add),
    path("depart/delete/", project1_views.depart_delete),
    path("depart/<int:nid>/edit/", project1_views.depart_edit),
    path("depart/search/", project1_views.department_search),
    path("user/list1/", project1_views.user_list1),
    path("user/add1/", project1_views.user_add1),
    path("user/model/form/add/", project1_views.user_model_form_add),
]
