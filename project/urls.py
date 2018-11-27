"""adminems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from app2 import views

urlpatterns = [

    path('index/', views.showindex),
    path('head/', views.head),
    path('menu/', views.menu),


    path('admin_login/', views.admin_login),
    path('admin_login_details/', views.admin_login_details),

    path('course/', views.course),
    path('addcourse/', views.addcourse),
    path('addcoursedetails/', views.addcoursedetails),
    path('coursecsv/', views.cousecsvfile),
    path('coursedelete/', views.coursedelete),
    path('courseupdate/', views.courseupdate),
   #path('courseimage/', views.courseupdate),

    path('faculity1/', views.faculity1),
    path('addfaculity/', views.addfaculity),
    path('addfaculitydetails/', views.addfaculitydetails),
    path('faculitycsv/', views.faculitycsvfile),
    path('faculitydelete/', views.faculitydelete),
    path('faculityupdate/', views.faculityupdate),
    #path('faculityimage/', views.faculityimage),

    path('student/', views.student1),
    path('viewstudent/', views.viewstudent),
    path('studentdetails/', views.studentdetails),
    path('studentlogin/', views.studentlogin),
    path('studentlogindetails/', views.studentlogindetails),
    path('studentwelcome/', views.studentwelcomedetails),
    path('studentdelete/', views.studentdelete),
    path('studentupdate/', views.studentupdate),
    path('studentcsv/', views.studentcsvfile),

    path('company/', views.company),
    path('company1/', views.company1),
    path('companydetails/', views.companydetails),
    path('companycsvfile/', views.companycsvfile),
    #path('companyapprove/', views.companyapprove),
    #path('companydecline/', views.companydecline),




]
