"""newsite URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.views.generic.base import RedirectView
urlpatterns = [
    url(r'^$', views.Login.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='../static/img/favicon.ico')),
    url(r'^time',views.time),
    url(r'^student_index',views.student_index),
    url(r'^student_edit/', views.student_edit),

    url(r'^admindelete/', views.admindelete),
    url(r'^coachdelete/', views.coachdelete),

    url(r'^admin_index', views.admin_index),
    url(r'^admin_coach/', views.admin_coach),
    url(r'^admin_coach_edit', views.admin_coach_edit),

    url(r'^admin_item/',views.admin_item),
    url(r'^admin_item_edit', views.admin_item_edit),

    url(r'^coach_index', views.coachs_index),
    url(r'^coach_student/', views.coach_student),
    url(r'^single_chart/', views.single_chart),

    url(r'^coach_search_student/', views.coach_search_student),
    url(r'^coach_student_edit/', views.coach_student_edit),
    url(r'^coach_search_result/',views.coach_search_result),
    url(r'^coach_inputdata/', views.coach_inputdata),
    #    url(r'^action', views.action),
    url(r'^system/',views.system),
    url(r'^coach/',views.coach),
    url(r'^data',views.data),
    url(r'^user/',views.user),
    url(r'^userdelete',views.userdelete),
    url(r'^useredit',views.useredit),

    url(r'^usersearch/',views.usersearch),
    url(r'^usersearchresult/', views.usersearchresult),
    url(r'^useredit/', views.useredit),

    url(r'^login',views.Login.as_view()),
#    url(r'^loginaction', views.loginaction),
    url(r'^signout', views.signout),

    url(r'^register.html',views.register),
    url(r'^registeraction.html',views.registeraction),

    url(r'^mysetting.html', views.mysetting),
    url(r'^imgtest.html$',views.imgtest),
    url(r'^imgtestajax.html', views.imgtestajax),

    url(r'^test', views.test),
    url(r'^base', views.base),
    url(r'^ajax/', views.ajax),
    url(r'^ajaxtest/', views.reajax),
    url(r'^jsonp.html',views.jsonp),
    url(r'^logtest/', views.logtest)
]
handler404 = views.page_not_found