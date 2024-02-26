https://www.cnblogs.com/wu-chao/p/8353315.html
https://www.cnblogs.com/tuyin/p/17142353.html#_label6   学习笔记


1.pip install django
2.django-admin startproject your_project_name
3.cd your_project_name


manage.py    项目管理 启动 创建APP 数据管理等 
setting.py   项目配置
urls.py      URL和函数的对应关系


 python manage.py startapp app01  就可以创建一个目录
 app01中tests.py 单元测试
 views.py  重要 函数  对应urls.py 
 model.py  重要  对数据库操作


 第一步去 setting中注册"app01.apps.App01Config",
 第二步  去urls.py中 编写和APP01中view视图函数的对应关系
 启动项目  python manage.py runserver
 http://127.0.0.1:8000/index/  就可以启动了·必须加index/

 如果在setting中# import os   'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 将模板文件夹添加到 DIRS 列表中
 view中的类似于template 中的文件  就不局限于在APP01中去寻找··也可以在外边

静态文件包括js img css 放到static文件夹下·

https://www.bilibili.com/video/BV1rT4y1v7uQ?p=40&vd_source=413156abd15e0c3b90d95acfcc909e36
17分



为新项目创建虚拟环境： python manage.py runserver

在新项目的目录中打开终端。
运行 python -m venv venv 创建虚拟环境。
激活虚拟环境：

在 Windows 上：venv\Scripts\activate
在 macOS/Linux 上：source venv/bin/activate。
安装 Django：

在虚拟环境中运行 pip install django
pip install requests


在虚拟环境下·安装数据库pip install mysqlclient

https://www.youtube.com/watch?v=o9VOTIJAY3k  这个网站告诉如何连接  启动workbench or 启动 mysql command line cliend
 我创建了一个 firstdjango的文件
 CREATE DATABASE django1 执行  在刷新 数据库就会出现在workbench上
 SHOW DATABASES 刷新就会出现在你的数据库表中


 然后在Django中的setting文件中设置数据库等信息 并且虚拟环境中 
 python manage.py makemigrations
 python manage.py migrate

 然后在workbench中 USE 数据库的名字  SHOW TABLES 就会出现数据的表Django

 show tables
 desc app01_uderinfo;
每次在model文件中添加或者删除新的数据库表·都需要从新启动一下·
 python manage.py makemigrations
 python manage.py migrate
 如果在已有的table中加一个新的字段··你执行命令时会出现提示2个选中  1.在terminal中输入新值  2 在code代码中列如
 age= models.IntegerField（default=值） 3.为空age= models.IntegerField（null=True,blank=True）


 Department.objects.create(title:"salele depatment")
            Department.objects.create(title:"education")
            Department.objects.create(title:"admintion")
 Department.objects.create(title:"salele depatment")
 Department.objects.create(title:"salele depatment")
在view中新增数据  在数据库中select * from app01_Department;就可以查询


