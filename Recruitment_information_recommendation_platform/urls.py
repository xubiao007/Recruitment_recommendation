"""Recruitment_information_recommendation_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url

from . import view


urlpatterns = [
    path('admin/', admin.site.urls),  # Django默认的后台管理

    url(r'^$', view.home_page, name='index'),  # 设置默认首页面

    path('captcha/',include('captcha.urls')),  # 验证码
    # 路由分发
    path('user/', include('User_information.urls')), # 用户相关信息

    path('task/', include('Reptile_task.urls')), # 处理爬虫任务数据管理

    path('job/', include('Job_information.urls')), # 爬取的基本招聘信息

    path('detail/', include('Detail_job_info.urls')), # 爬取的详细招聘信息

    path('collection/', include('Collection_management.urls')), # 收藏管理

    path('recommend/', include('Recommended_information.urls')), # 推荐信息管理

    path('analysis/', include('Data_image.urls')), # 图像分析 和 职位云图
]
