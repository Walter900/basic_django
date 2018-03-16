"""sample2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [

  url(r'^$',views.index),
  url(r'^getTest1/$',views.getTest1),
  url(r'^getTest2/$',views.getTest2),
  url(r'^post1/$', views.post1),
  url(r'^post2/$', views.post2),
  url(r'^cookieTest/$',views.cookietest),
  url(r'^redTest1/$',views.redTest1),
  url(r'^redTest2/$',views.redTest2),
  url(r'^session1/$', views.session1),
  url(r'^session2/$', views.session2),
  url(r'^session2_handle/$', views.session2_handle),
  url(r'^session3/$', views.session3),
  url(r'^verifycode/$', views.verifycode),
  url(r'^verifyTest1/$', views.verifyTest1),
  url(r'^verifyTest2/$', views.verifyTest2)

]
