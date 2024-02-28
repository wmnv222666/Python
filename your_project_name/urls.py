from django.contrib import admin
from django.urls import path
from project1 import views as project1_views

urlpatterns = [
    # path("admin/", admin.site.urls),
   
    path("depart/list/", project1_views.depart_list),
    path("depart/add/", project1_views.depart_add),
    path("depart/delete/", project1_views.depart_delete),
    path("depart/<int:nid>/edit/", project1_views.depart_edit),
    path("depart/search/", project1_views.department_search),
    path("user/list1/", project1_views.user_list1),
    path("user/add1/", project1_views.user_add1),
    path("user/model/form/add/", project1_views.user_model_form_add),
]
