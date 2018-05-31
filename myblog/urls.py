"""myblog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_view
from learn import views as learn_view

urlpatterns = [
    url(r'^add/$', blog_view.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/$', blog_view.add2, name='add2'),
    url(r'^$', blog_view.index),
    url(r'addform/$', blog_view.addform,name='addform'),
    url(r'postform/$', blog_view.post_form,name='postform'),
    url(r'index2/$', blog_view.home,name='index2'),
    url(r'home2/$', blog_view.home2,name='home2'),
    url(r'home3/$', blog_view.home3,name='home3'),
    url(r'home4/$', blog_view.home4,name='home4'),
    url(r'home5/$', blog_view.home5,name='home5'),
    url(r'home6/$', blog_view.home6,name='home6'),
    url(r'showall/$', blog_view.show_all_data,name='showall'),
    url(r'home/$', learn_view.home,name='home'),
    url(r'^admin/', admin.site.urls),
]
