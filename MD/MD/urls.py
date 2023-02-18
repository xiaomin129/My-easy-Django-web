"""MD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/', views.index),#员工信息
    path('login/',views.login),#登陆
    path('index/drugs_in/',views.drugs_in),#员工进货
    path('index/drugs_out/',views.drugs_out),#员工销售
    path('index/drugs_index/',views.drugs_index),#药品库存
    path('index/log/',views.log),#员工日志
    path('manage_index/',views.manage_index),#管理员信息
    path('manage_log/',views.manage_log),#管理员日志
    path('exit/',views.exit),#注销
    path('manage_index/drugs/',views.drugs_index),#管理员库存
    path('manage_index/worker/',views.woker_info),#管理员工信息
    path('manage_index/god/',views.god),#购买记录
    path('add_worker/',views.add_worker),#添加员工
    path('del_worker/',views.del_worker),#删除员工
    path('cookie/',views.cookie)#测试
]
