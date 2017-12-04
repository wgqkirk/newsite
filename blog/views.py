from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from blog import models

# Create your views here.

import datetime
def addbool(request):
    return HttpResponse('添加成功')

def time(request):
    t=datetime.datetime.now()

    return render(request,'time.html',{'ctime':t})

def index(request):
    return render(request,'index.html')
def tag(request):
    return render(request,'tag.html')
def user(request):
    return render(request,'user.html')
def usersearch(request):
    return render(request,'usersearch.html')
def content(request):
    return render(request,'content.html')
def contentpost(request):
    return render(request,'contentpost.html')
user_list=[]

def login(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        password = request.POST.get('password', None)
        user={'username':username,'password':password}
        #user_list.append(user)
        models.userstest.objects.create(
            name=username,
            password=password,
        )
        info_list=models.userstest.objects.all()
        return render(request,'login.html',{'user_list':info_list})
    return render(request,'login.html')