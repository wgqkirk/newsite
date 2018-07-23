from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django import views
import json
from django import forms
from django.views.decorators.csrf import csrf_exempt
from blog import models
import hashlib
from utils.pageation import page_help
from utils.my_function import *
# Create your views here.


class RegisterForm(forms.Form):
    username=forms.CharField(min_length=2,error_messages={'required':'用户名不能为空','min_length':'长度不能少于2'})
    email = forms.EmailField(error_messages={'required':'邮箱不能为空','min_length':'长度不能少于2','ivalid':'邮箱格式错误'})
    password=forms.CharField(min_length=6, error_messages={'required':'密码不能为空','min_length':'长度不能少于6'})

class LoginForm(forms.Form):
    user=forms.CharField(min_length=2, error_messages={'required':'用户名不能为空','min_length':'长度不能少于2'})
    password = forms.CharField(min_length=6, error_messages={'required':'密码不能为空','min_length':'长度不能少于6'})



import datetime
def addbool(request):
    return HttpResponse('添加成功')

def time(request):
    t = datetime.datetime.now()

def page_not_found(request):
    return render(request, 'error404.html')

    return render(request, 'time.html', {'ctime':t})
def signout(request):
    del request.session['username']
    return redirect('/login.html')
# def action(request):
#     if request.method=='POST':
#         username=request.POST.get('username',None)
#         m1 = hashlib.md5()
#         # m1.update('wgq1360169汪国强')
#         # print(m1.hexdigest())
#         m1.update(request.POST.get('password', None).encode('utf-8'))
#         password = m1.hexdigest()
#         info={'username':username,'password':password}
#         if models.userinfo.objects.filter(**info).exists():
#
#             #print("this",request.session.get('username'))
#             #rep=redirect('/student_index.html')
#             request.session['username'] = username
#             return render(request,'student_index.html')
#         else:
#             flag=True
#             return render(request,'login.html',locals())
def student_index(request):
    pageusername = request.session.get('username')
    if pageusername:
        query_set = models.userinfo.objects.filter(username=pageusername)
        for i in query_set:
            the_id = i.choice_id
            the_name = i.choice
        usercount = models.userinfo.objects.filter(choice_id=the_id).count()
        malecount = models.userinfo.objects.filter(choice_id=the_id).filter(gender='男').count()
        femalecount = models.userinfo.objects.filter(choice_id=the_id).filter(gender='女').count()
        query_set1 = models.item.objects.filter(id=the_id)
        for i in query_set1:
            item_cost = i.itemcost
            item_time = i.itemtime
        weekinfo=None
        jugweek8 = models.weekly_info.objects.get(username=pageusername).week8
        userinfo = models.weekly_info.objects.get(username=pageusername)
        week0=userinfo.week0
        week1=userinfo.week1
        week2 = userinfo.week2
        week3 = userinfo.week3
        week4 = userinfo.week4
        week5 = userinfo.week5
        week6 = userinfo.week6
        week7 = userinfo.week7
        week8 = userinfo.week8
        if jugweek8:
            weekinfo=[week0,week1,week2,week3,week4,week5,week6,week7,week8]
        else:
            if models.weekly_info.objects.get(username=pageusername).week7:
                weekinfo=[week0,week1,week2,week3,week4,week5,week6,week7]
            else:
                if models.weekly_info.objects.get(username=pageusername).week6:
                    weekinfo = [week0,week1,week2,week3,week4,week5,week6]
                else:
                    if models.weekly_info.objects.get(username=pageusername).week5:
                        weekinfo = [week0,week1,week2,week3,week4,week5]
                    else:
                        if models.weekly_info.objects.get(username=pageusername).week4:
                            weekinfo = [week0,week1,week2,week3,week4]
                        else:
                            if models.weekly_info.objects.get(username=pageusername).week3:
                                weekinfo = [week0,week1,week2,week3]
                            else:
                                if models.weekly_info.objects.get(username=pageusername).week2:
                                    weekinfo = [week0,week1,week2]
                                else:
                                    if models.weekly_info.objects.get(username=pageusername).week1:
                                        weekinfo = [week0,week1]
                                    else:
                                        if models.weekly_info.objects.get(username=pageusername).week0:
                                            weekinfo = [week0]
        return render(request, 'student_index.html', locals())
    else:
        return redirect('/login.html')

def student_edit(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method=='GET':
            userset=models.userinfo.objects.get(username=pageusername,)
            item_set = models.item.objects.all()
            return render(request, 'student_edit.html', locals())
        elif request.method=='POST':
            uid=request.POST.get('id')
            username = request.POST.get('username')
            m1 = hashlib.md5()
            password_org=request.POST.get('pwd', None)
            m1.update(password_org.encode('utf-8'))
            password = m1.hexdigest()
            gender = request.POST.get('gender')
            birth = request.POST.get('birth')
            email=request.POST.get('email')
            obj=models.userinfo.objects.get(username=pageusername)
            obj.username=username
            if request.POST.get('pwd'):
                obj.password=password
            obj.birth=birth
            obj.gender=gender
            obj.email=email
            if request.POST.get('choice'):
                choice = int(request.POST.get('choice'))
                new_obj=models.user_now.objects.get(uid=uid)
                new_obj.choice_id=choice
                new_obj.save()
                obj.choice_id=choice
            obj.save()
            return redirect('student_edit.html')
def admindelete(request):
    pageusername = request.session.get('username')
    uid = request.POST.get('uid', None)
    print(uid)
    delete_username=models.admin.objects.get(uid=uid).username
    if pageusername==delete_username:
        return HttpResponse('disabled')
    else:
        models.admin.objects.filter(uid=uid,).delete()
        return HttpResponse('deleted')
def coachdelete(request):
    uid = request.POST.get('uid', None)
    print(uid)
    models.coach.objects.filter(uid=uid,).delete()
    return HttpResponse('deleted')
def admin_index(request):
    pageusername=request.session.get('username')
    if pageusername:
        if request.method == 'POST':
            username=request.POST.get('username')
            if models.admin.objects.filter(username=username).exists():
                info='该用户已重复'
                current_page = int(request.GET.get('pagenum', 1))
                total = models.admin.objects.all().count()

                obj = page_help('/admin_index/', current_page, total, 10)
                page = obj.page_str()
                query_set = models.admin.objects.all()[obj.db_start():obj.db_end()]
                return render(request, 'admin_index.html', locals())
            else:
                usernames = request.POST.get('username')
                m1 = hashlib.md5()
                m1.update(request.POST.get('pwd').encode('utf-8'))
                password = m1.hexdigest()
                registertime = datetime.datetime.now()
                user = {'username': usernames, 'password': password,  'registerdate': registertime}
                models.admin.objects.create(**user)
                # 获取到当前页码
                current_page = int(request.GET.get('pagenum', 1))
                total = models.admin.objects.all().count()

                obj = page_help('/admin_index', current_page, total, 10)
                page = obj.page_str()
                query_set = models.admin.objects.all()[obj.db_start():obj.db_end()]

                return render(request, 'admin_index.html', locals())
        elif request.method=="GET":
            # 获取到当前页码
            current_page = int(request.GET.get('pagenum', 1))
            total = models.admin.objects.all().count()
            obj = page_help('/admin_index', current_page, total, 10)
            page = obj.page_str()
            query_set = models.admin.objects.all()[obj.db_start():obj.db_end()]
            return render(request, 'admin_index.html', locals())
    else:
        return redirect('/login.html')
def admin_coach(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method == 'POST':
            username = request.POST.get('username')
            if models.coach.objects.filter(username=username).exists():
                info='该用户已重复'
                current_page = int(request.GET.get('pagenum', 1))
                total = models.coach.objects.all().count()
                obj = page_help('/admin_coach/', current_page, total, 10)
                page = obj.page_str()
                query_set = models.coach.objects.all()[obj.db_start():obj.db_end()]
                item_set = models.item.objects.all()
                return render(request, 'admin_coach.html', locals())
            else:
                m1 = hashlib.md5()
                m1.update(request.POST.get('pwd', None).encode('utf-8'))
                password = m1.hexdigest()
                gender = request.POST.get('gender')
                birth = request.POST.get('birth')
                tel = request.POST.get('tel')
                charge = int(request.POST.get('charge'))
                registertime = datetime.datetime.now()
                print(username, password, gender,tel, birth,registertime)
                user = {'username': username, 'password': password, 'gender': gender, 'birth': birth,'tel':tel,  'registerdate': registertime,'charge_id':charge}
                models.coach.objects.create(**user)
                # 获取到当前页码
                current_page = int(request.GET.get('pagenum', 1))
                total = models.coach.objects.all().count()
                obj = page_help('/admin_coach/', current_page, total, 10)
                page = obj.page_str()
                query_set = models.coach.objects.all()[obj.db_start():obj.db_end()]
                return render(request, 'admin_coach.html', locals())
        elif request.method=='GET':
            # 获取到当前页码
            current_page = int(request.GET.get('pagenum', 1))
            total = models.coach.objects.all().count()
            obj = page_help('/admin_coach/', current_page, total, 10)
            page = obj.page_str()
            query_set = models.coach.objects.all()[obj.db_start():obj.db_end()]
            item_set=models.item.objects.all()
            return render(request, 'admin_coach.html', locals())
    else:
        return redirect('/login.html')

def admin_coach_edit(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method=='GET':
            uid = request.GET.get('uid', None)
            print(uid)
            info=models.coach.objects.get(uid=uid,)
            item_set = models.item.objects.all()
            return render(request, 'admin_coach_edit.html', locals())
        elif request.method=='POST':
            uid=request.POST.get('uid')
            username = request.POST.get('username')
            m1 = hashlib.md5()
            m1.update(request.POST.get('pwd', None).encode('utf-8'))
            password = m1.hexdigest()
            gender = request.POST.get('gender')
            birth = request.POST.get('birth')
            charge = int(request.POST.get('charge'))
            obj=models.coach.objects.get(uid=uid)
            obj.username=username
            obj.password=password
            obj.birth=birth
            obj.gender=gender
            obj.charge_id=charge
            obj.save()
            return redirect('/admin_coach/')
    else:
        return redirect('/login.html')


def admin_item(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method == 'POST':
            itemname = request.POST.get('itemname')
            itemcost = request.POST.get('itemcost')
            itemtime = request.POST.get('itemtime')
            print(itemname, itemcost, itemtime)
            user = {'itemname': itemname, 'itemcost': itemcost, 'itemtime': itemtime}
            models.item.objects.create(**user)
            # 获取到当前页码
            current_page = int(request.GET.get('pagenum', 1))
            total = models.item.objects.all().count()
            obj = page_help('/admin_item', current_page, total, 10)
            page = obj.page_str()
            query_set = models.item.objects.all()[obj.db_start():obj.db_end()]

            return render(request, 'admin_item.html', locals())
        else:
            # 获取到当前页码
            current_page = int(request.GET.get('pagenum', 1))
            total = models.item.objects.all().count()
            obj = page_help('/admin_item', current_page, total, 10)
            page = obj.page_str()
            query_set = models.item.objects.all()[obj.db_start():obj.db_end()]
            return render(request, 'admin_item.html', locals())


def admin_item_edit(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method=='GET':
            id = request.GET.get('id', None)
            print(id)
            info=models.item.objects.get(id=id,)
            return render(request, 'admin_item_edit.html', locals())
        elif request.method=='POST':
            id=request.POST.get('id')
            itemname = request.POST.get('itemname')
            itemcost = request.POST.get('itemcost')
            itemtime = request.POST.get('itemtime')

            obj=models.item.objects.get(id=id)
            obj.itemname=itemname
            obj.itemcost=itemcost
            obj.itemtime=itemtime
            obj.save()
            return redirect('/admin_item/')
    else:
        return redirect('/login.html')

def coachs_index(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method == 'GET':
            query_set = models.coach.objects.filter(username=pageusername)
            for i in query_set:
                the_id = i.charge_id
                the_name=i.charge
            usercount = models.userinfo.objects.filter(choice_id=the_id).count()
            malecount=models.userinfo.objects.filter(choice_id=the_id).filter(gender='男').count()
            femalecount = models.userinfo.objects.filter(choice_id=the_id).filter(gender='女').count()
            query_set1=models.item.objects.filter(id=the_id)
            for i in query_set1:
                item_cost=i.itemcost
                item_time=i.itemtime
            query_set2=list(models.user_now.objects.filter(choice_id=the_id).values_list('username','weight'))
            print(query_set2)
            name_list=[]
            weight_list=[]
            for i in query_set2:
                name_list.append(i[0])
                weight_list.append(int(i[1]))
            print(name_list)
            print(weight_list)
            query_set2_userinfo=list(models.userinfo.objects.filter(choice_id=the_id).values_list('username','weight'))
            print(query_set2_userinfo)
            weight_list_userinfo=[]
            name_list_userinfo=[]
            for i in query_set2_userinfo:
                name_list_userinfo.append(i[0])
                weight_list_userinfo.append(int(i[1]))
            print(name_list_userinfo,weight_list_userinfo)
            return render(request, 'coach_index.html', locals())
    else:
        return redirect('/login.html')

def coach_student(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method=='GET':
            query_set = models.coach.objects.filter(username=pageusername)
            for i in query_set:
                the_id = i.charge_id
                the_name = i.charge
            # 获取到当前页码
            current_page = int(request.GET.get('pagenum', 1))
            total = models.userinfo.objects.filter(choice_id=the_id).count()
            obj = page_help('/coach_student/', current_page, total, 10)
            page = obj.page_str()
            query_set = models.userinfo.objects.filter(choice_id=the_id)[obj.db_start():obj.db_end()]
            return render(request, 'coach_student.html', locals())
    else:
        return redirect('/login.html')
def coach_student_edit(request):
    pageusername = request.session.get('username')
    if pageusername:
        if request.method=='GET':
            uid = request.GET.get('uid', None)
            print(uid)
            info=models.userinfo.objects.get(uid=uid,)
            item_set = models.item.objects.all()
            return render(request, 'coach_student_edit.html', locals())
        elif request.method=='POST':
            uid=request.POST.get('uid')
            username = request.POST.get('username')
            m1 = hashlib.md5()
            password_org=request.POST.get('pwd', None)
            m1.update(password_org.encode('utf-8'))
            password = m1.hexdigest()
            gender = request.POST.get('gender')
            birth = request.POST.get('birth')
            email=request.POST.get('email')
            print(request.POST.get('choice'))

            obj=models.userinfo.objects.get(uid=uid)
            id = obj.id
            obj_user_now=models.user_now.objects.get(uid=id)
            obj_weekly_info=models.weekly_info.objects.get(uid=id)
            obj.username=username
            obj_user_now.username=username
            obj_weekly_info.username=username
            if request.POST.get('pwd'):
                obj.password=password
            obj.birth=birth
            obj.gender=gender
            obj.email=email
            if request.POST.get('choice'):
                choice = int(request.POST.get('choice'))
                obj_user_now.choice_id=choice
                obj_weekly_info.choice_id=choice
                obj_user_now.save()
                obj_weekly_info.save()
                obj.choice_id=choice
            obj.save()
            obj_user_now.save()
            obj_weekly_info.save()
            return redirect('/coach_student/')
    else:
        return redirect('/login.html')
def single_chart(request):
    pageusername = request.session.get('username')
    if pageusername:
        uid=request.GET.get('uid')
        print(uid)
        userset=models.userinfo.objects.filter(uid=uid,)
        userset=userset[0]
        userheight=userset.height
        id=userset.id
        print(userheight)
        userinfo=models.weekly_info.objects.filter(uid=id,)
        userinfo=userinfo[0]
        userweight=[userinfo.week0,userinfo.week1,userinfo.week2,userinfo.week3,userinfo.week4,userinfo.week5,userinfo.week6,userinfo.week7,userinfo.week8]

        #去除list里的None值,使其转成weight
        userweight=make_weight_list(userweight)
        colorlist=['#DC143C','#800080','#483D8B','#000080','#00BFFF','#00FFFF','#00FA9A','#006400','#FFFAF0']
        pielist=[]
        weight_now=userweight[-1]
        for i in range(len(userweight)):
            if i <len(userweight)-1:
                item={'num':i+1,'loseweight':userweight[i]-userweight[i+1],'weeknum':'第%s周'%(i+1),'color_16':colorlist[i]}
                pielist.append(item)
        print(pielist,weight_now)

        max_weight=max(userweight)
        min_weight=min(userweight)

        #改变list里的值，使其转成bmi
        userbmi=make_bmi(userheight,userweight)
        max_bmi=max(userbmi)
        min_bmi=min(userbmi)



        return render(request, 'single_chart.html', locals())
    else:
        return redirect('/login.html')


def coach_search_student(request):
    pageusername = request.session.get('username')
    if pageusername:
        return render(request, 'coach_search_student.html', locals())
    else:
        return redirect('/login.html')

from django.db.models import Q
def coach_search_result(request):
    pageusername = request.session.get('username')
    print('11111')
    if pageusername:
        user_list=models.userinfo.objects.all()
        queryset = models.coach.objects.filter(username=pageusername)
        for i in queryset:
            the_id = i.charge_id
            user_list=user_list.filter(choice_id=the_id)
        searchname=request.POST.get('username',None)
        if searchname:
            user_list=user_list.filter(username__icontains=searchname)
        searchgender=request.POST.get('gender',None)
        if searchgender !='空':
            user_list=user_list.filter(gender=searchgender)
        height_low=request.POST.get('height_low',None)
        if height_low:
            user_list=user_list.filter(height__gte=height_low)
        height_high=request.POST.get('height_high',None)
        if height_high:
            user_list=user_list.filter(height__lte=height_high)
        weight_sm=request.POST.get('weight_sm',None)
        if weight_sm:
            user_list=user_list.filter(weight__gte=weight_sm)
        weight_lg=request.POST.get('weight_lg',None)
        if weight_lg:
            user_list = user_list.filter(weight__lte=weight_lg)

        print(user_list)

        return render(request, 'coach_search_result.html', locals())

    else:
        return redirect('/login.html')

def coach_inputdata(request):
    pageusername = request.session.get('username')
    if pageusername:
        queryset = models.coach.objects.filter(username=pageusername)
        for i in queryset:
            the_id = i.charge_id
        if request.method=='GET':
            user_list = models.weekly_info.objects.filter(choice_id=the_id)
            return render(request, 'coach_inputdata.html', locals())
        elif request.method=='POST':
            uid = request.POST.get('userid')
            weight = request.POST.get('weight')
            week=request.POST.get('FieldName')
            beizhu=request.POST.get('beizhu')
            uid=uid.split('#')
            weight=weight.split('#')
            beizhu=beizhu.split('#')
            print(uid,weight,week,beizhu)
            for i in range(len(uid)):
                the_uid=int(uid[i])
                if weight[i]=='':
                    input_weight=None
                else:
                    input_weight=float(weight[i])

                updataweekinfo(the_uid,input_weight,week,beizhu[i])
                updateusernow(the_uid,input_weight)
            return HttpResponse('already done')
    else:
        return redirect('/login.html')
def updateusernow(uid,weight):
    if weight:
        myobj = models.user_now.objects.get(uid=uid)
        myobj.weight = weight
        myobj.save()

def updataweekinfo(uid,weight,week,beizhu):
    if week=='week1':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week1 = weight
        myobj.week1_suggest=beizhu
        myobj.save()
    elif week=='week2':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week2 = weight
        myobj.week2_suggest = beizhu
        myobj.save()
    elif week=='week3':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week3 = weight
        myobj.week3_suggest = beizhu
        myobj.save()
    elif week=='week4':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week4 = weight
        myobj.week4_suggest = beizhu
        myobj.save()
    elif week=='week5':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week5 = weight
        myobj.week5_suggest = beizhu
        myobj.save()
    elif week=='week6':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week6 = weight
        myobj.week6_suggest = beizhu
        myobj.save()
    elif week=='week7':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week7 = weight
        myobj.week7_suggest = beizhu
        myobj.save()
    elif week=='week8':
        myobj = models.weekly_info.objects.get(uid=uid)
        myobj.week8 = weight
        myobj.week8_suggest = beizhu
        myobj.save()
def data(request):
    username=request.session.get('username')
    myinde = request.session.get('indentify')
    if myinde == '管理员':
        manager = True
        coach = True
        comuser = True
    elif myinde == '教练':
        coach = True
        comuser = True
    elif myinde == '会员':
        comuser = True
    else:
        manager = False
        coach = False
        comuser = False
    if username:
        return render(request, 'data.html', locals())
    else:
        return redirect('/login.html')
def user(request):
    username = request.session.get('username')
    myinde = request.session.get('indentify')
    if myinde == '管理员':
        manager = True
        coach = True
        comuser = True
    elif myinde == '教练':
        coach = True
        comuser = True
    elif myinde == '会员':
        comuser = True
    else:
        manager = False
        coach = False
        comuser = False
    if username:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('pwd')
            gender=request.POST.get('gender')
            age=request.POST.get('age')
            weight=request.POST.get('weight')
            height=request.POST.get('height')
            email=request.POST.get('email')
            rank=int(request.POST.get('rank'))
            registertime = datetime.datetime.now()

            print(username,password,gender,age,weight,height,email,rank,registertime)
            user = {'username': username, 'password': password, 'gender': gender, 'age': age, 'weight': weight,
                    'height': height, 'email': email, 'rank_id': rank, 'registerdate': registertime}
            models.userinfo.objects.create(**user)
            # 获取到当前页码
            current_page = int(request.GET.get('pagenum', 1))
            total = models.userinfo.objects.all().count()
            obj = page_help('/user', current_page, total, 10)
            page = obj.page_str()
            query_set = models.userinfo.objects.all()[obj.db_start():obj.db_end()]

            return render(request, 'user.html', locals())
        else:
            #获取到当前页码
            current_page=int(request.GET.get('pagenum',1))
            total=models.userinfo.objects.all().count()
            obj=page_help('/user',current_page,total,10)
            page=obj.page_str()
            query_set = models.userinfo.objects.all()[obj.db_start():obj.db_end()]

            return render(request, 'user.html', locals())
    else:
        return redirect('/login.html')

def userdelete(request):
    userid = request.POST.get('id', None)
    print(userid)
    models.userinfo.objects.filter(id=userid,).delete()
    models.user_now.objects.filter(uid=userid,).delete()
    models.weekly_info.objects.filter(id=userid, ).delete()
    return HttpResponse('deleted')

def usersearch(request):
    username = request.session.get('username')
    if username:
        return render(request, 'usersearch.html', locals())
    else:
        return redirect('/login.html')
def usersearchresult(request):
    username = request.session.get('username')
    myinde = request.session.get('indentify')
    if myinde == '管理员':
        manager = True
        coach = True
        comuser = True
    elif myinde == '教练':
        coach = True
        comuser = True
    elif myinde == '会员':
        comuser = True
    else:
        manager = False
        coach = False
        comuser = False
    if username:
        searchname=request.POST.get('username',None)
        searchid=request.POST.get('userid',None)
        searchrank=request.POST.get('choice',None)


        # 获取到当前页码
        # current_page = int(request.POST.get('pagenum', 1))
        # total = models.userinfo.objects.all().count()
        # from utils.pageation import page_help
        # obj = page_help('/usersearchresult', current_page, total, 10)
        # page = obj.page_str()
        # query_set = models.userinfo.objects.all()[obj.db_start():obj.db_end()]


        if searchname=='':
            if searchid=='':
                if searchrank=='空':
                    query_set = models.userinfo.objects.all()
                else:
                    print(searchrank)
                    query_set = models.userinfo.objects.filter(rank__rank_name__icontains=searchrank)

            else:
                if searchrank=='空':
                    query_set = models.userinfo.objects.filter(id__icontains=searchid)
                else:
                    print(searchid,searchrank)
                    query_set = models.userinfo.objects.filter(id__icontains=searchid).filter(rank__rank_name__icontains=searchrank)
                for i in query_set:
                    print(i)
        else:
            if searchid=='':
                if searchrank=='空':
                    query_set = models.userinfo.objects.filter(username__icontains=searchname)
                else:
                    print(searchname,searchrank)
                    query_set= models.userinfo.objects.filter(username__icontains=searchname).filter(rank__rank_name__icontains=searchrank)
            else:
                if searchrank=="空":
                    query_set = models.userinfo.objects.filter(username__icontains=searchname).filter(
                        id__icontains=searchid)
                else:
                    print(searchname,searchid,searchrank)
                    query_set = models.userinfo.objects.filter(username__icontains=searchname).filter(id__icontains=searchid).filter(rank__rank_name__icontains=searchrank)

        if len(query_set)==0:
            flag=True
        return render(request, 'usersearchresult.html', locals())

    else:
        return redirect('/login.html')

def useredit(request):
    username = request.session.get('username')
    myinde = request.session.get('indentify')
    if myinde == '管理员':
        manager = True
        coach = True
        comuser = True
    elif myinde == '教练':
        coach = True
        comuser = True
    elif myinde == '会员':
        comuser = True
    else:
        manager = False
        coach = False
        comuser = False
    if username:
        if request.method=='GET':
            userid = request.GET.get('userid', None)
            print(userid)
            info=models.userinfo.objects.get(id=userid,)
            return render(request, 'useredit.html', locals())
        else:
            userid=request.POST.get('userid')
            username = request.POST.get('username')
            m1 = hashlib.md5()
            m1.update(request.POST.get('pwd', None).encode('utf-8'))
            password = m1.hexdigest()
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            email = request.POST.get('email')
            rank = int(request.POST.get('rank'))
            obj=models.userinfo.objects.get(id=userid)
            obj.username=username
            obj.password=password
            obj.eamil=email
            obj.age=age
            obj.weight=weight
            obj.height=height
            obj.gender=gender
            obj.rank_id=rank
            obj.save()
            return redirect('/user/')
    else:
        return redirect('/login.html')
def system(request):
    username = request.session.get('username')
    myinde = request.session.get('indentify')
    if myinde == '管理员':
        manager = True
        coach = True
        comuser = True
    elif myinde == '教练':
        coach = True
        comuser = True
    elif myinde == '会员':
        comuser = True
    else:
        manager = False
        coach = False
        comuser = False
    if username:
        return render(request, 'system.html', locals())
    else:
        return redirect('/login.html')
def coach(request):
    username = request.session.get('username')
    myinde = request.session.get('indentify')
    if myinde == '管理员':
        manager = True
        coach = True
        comuser = True
    elif myinde == '教练':
        coach = True
        comuser = True
    elif myinde == '会员':
        comuser = True
    else:
        manager = False
        coach = False
        comuser = False
    if username:
        return render(request, 'coach.html', locals())
    else:
        return redirect('/login.html')
user_list=[]

class Login(views.View):

    def get(self,request,*args,**kwargs):
        username = request.session.get('username', default='')
        return render(request, 'login.html', locals())
    def post(self,request):

        username = request.POST.get('username', None)
        print(username)
        m1 = hashlib.md5()
        # m1.update('wgq1360169汪国强')
        # print(m1.hexdigest())
        m1.update(request.POST.get('password', None).encode('utf-8'))
        password = m1.hexdigest()
        print(password)
        iden=request.POST.get('identify',None)
        print(iden)
        info = {'username': username, 'password': password}
        if iden=='admin':
            queryset=models.admin.objects.filter(**info)
        elif iden=='coach':
            queryset = models.coach.objects.filter(**info)
        elif iden=='student':
            queryset = models.userinfo.objects.filter(**info)
        if queryset.exists():
            request.session['username'] = username
            if iden == 'admin':
                return redirect('admin_index.html', locals())
            elif iden == 'coach':
                return redirect('coach_index.html', locals())
            elif iden == 'student':
                return redirect('student_index.html', locals())
        else:
            flag = True
            return render(request, 'login.html', locals())

# def login(request):
#     username = request.session.get('username', default='')
#     if request.method=='POST':
#         #print('111')
#         username=request.POST.get('username',None)
#         m1 = hashlib.md5()
#         # m1.update('wgq1360169汪国强')
#         # print(m1.hexdigest())
#         m1.update(request.POST.get('password', None).encode('utf-8'))
#         password = m1.hexdigest()
#         info={'username':username,'password':password}
#         if models.userinfo.objects.filter(**info).exists():
#
#             #print("this",request.session.get('username'))
#             #rep=redirect('/student_index.html')
#             request.session['username'] = username
#             return redirect('student_index.html')
#         else:
#             flag=True
#             return render(request,'login.html',locals())
#     #username = request.session.get('username',default='')
#     #print('username:',username)
#     return render(request,'login.html',locals())
# def loginaction(request):
#     if request.method=='POST':
#         print('111')
#         username=request.POST.get('username',None)
#         m1 = hashlib.md5()
#         # m1.update('wgq1360169汪国强')
#         # print(m1.hexdigest())
#         m1.update(request.POST.get('password', None).encode('utf-8'))
#         password = m1.hexdigest()
#         info={'username':username,'password':password}
#         if models.userinfo.objects.filter(**info).exists():
#
#             #print("this",request.session.get('username'))
#             #rep=redirect('/student_index.html')
#             #request.session['username'] = username
#             return redirect('student_index.html')
#         else:
#             flag=True
#             return render(request,'login.html',locals())
#     else:
#         return redirect('login.html')

def register(req):
    if req.method=='POST':
        username = req.POST.get('username', None)
        if username:
            info = {'username': username, }
            if models.userinfo.objects.filter(**info).exists():
                return HttpResponse('1')
            else:
                return HttpResponse('2')

        email=req.POST.get('email',None)
        if email:
            info2 = {'email': email, }
            if models.userinfo.objects.filter(**info2).exists():
                return HttpResponse('1')
            else:
                return HttpResponse('2')
    item_set = models.item.objects.all()
    return render(req, 'register.html', locals())

def registeraction(req):
    if req.method=='POST':
        obj = RegisterForm(req.POST)
        if obj.is_valid():
            value_dict=obj.clean()

            username = req.POST.get('username', None)
            email = req.POST.get('email', None)
            # print(email)
            m1 = hashlib.md5()
            # m1.update('wgq1360169汪国强')
            # print(m1.hexdigest())
            m1.update(req.POST.get('password', None).encode('utf-8'))
            password = m1.hexdigest()
            gender = req.POST.get('gender')
            weight = req.POST.get('weight')
            height = req.POST.get('height')
            birth = req.POST.get('birth')
            choice = int(req.POST.get('choice'))
            registertime = datetime.datetime.now()
            import uuid

            uid=uuid.uuid4()
            user = {'username': username, 'password': password, 'email': email,'gender': gender, 'birth': birth, 'weight': weight, 'height': height, 'choice_id':choice ,'registerdate': registertime,'uid':uid}

            # print(registertime)
            # user_list.append(user)
            models.userinfo.objects.create(**user)
            query_userinfo=models.userinfo.objects.filter(username=username)
            for i in query_userinfo:
                userinfo_uid=i.id
            user_now = {'username': username, 'weight': weight, 'height': height, 'choice_id': choice,'uid':userinfo_uid}
            models.user_now.objects.create(**user_now)
            weekly_info={'username': username, 'week0': weight, 'choice_id': choice,'uid':userinfo_uid}
            models.weekly_info.objects.create(**weekly_info)
            req.session['username'] = username

            return redirect('login.html')
        else:
            oo= obj
            item_set = models.item.objects.all()
        #   print(list(errorinfo['username'][0])[0])
            return render(req, 'register.html', locals())


import os
def mysetting(request):
    if request.method=='GET':
        return render(request, 'mysetting.html')
    elif request.method=='POST':
        return render(request, 'mysetting.html')

def imgtest(request):
    if request.method=='POST':
        name=request.POST.get('name')
        obj=request.FILES.get("img")
        print(name,obj.name,obj.size)
        imgsrc=os.path.join('blog/static/testimg',obj.name)
        # obj.chunks()将文件内容分成一一块的
        with open(imgsrc,'wb')as f:
            for i in obj.chunks():
                f.write(i)
        sqlpath=imgsrc.replace('blog','..')
        print(sqlpath)
        models.testimgsrc.objects.create(name=name,path=sqlpath)
        return redirect('imgtest.html')
    elif request.method=='GET':
        imglist=models.testimgsrc.objects.values('path')
        # print(imglist)
        return render(request, 'imgtest.html', {'imglist':imglist})

def imgtestajax(request):
    if request.method=='POST':
        name=request.POST.get('name')
        obj=request.FILES.get("img")
        print(name,obj.name,obj.size)
        imgsrc=os.path.join('blog/static/testimg',obj.name)
        # obj.chunks()将文件内容分成一一块的
        with open(imgsrc,'wb')as f:
            for i in obj.chunks():
                f.write(i)
        sqlpath=imgsrc.replace('blog','..')
        print(sqlpath)
        models.testimgsrc.objects.create(name=name,path=sqlpath)
        res={'status':True,'path':sqlpath}
        print(res)
        return HttpResponse(json.dumps(res))
    elif request.method=='GET':
        imglist=models.testimgsrc.objects.values('path')
        # print(imglist)
        return render(request, 'imgtestajax.html', {'imglist':imglist})

def test(req):
    uid=req.POST.get('userid')
    weight=req.POST.get('weight')
    print(uid,weight)

    # query_set=models.user_now.objects.all()
    #
    # for i in query_set:
    #     info = {'uid':i.uid,'username':i.username,'week0':i.weight,'choice_id':i.choice_id}
    #     key=i.username
    #     value=i.weight
    #     info[key]=value
    #
    #     print(info)
    #     models.weekly_info.objects.create(**info)
    return render(req, 'test.html')

def base(req):
    return render(req, 'base.html')
def ajax(req):
    return render(req, 'ajaxtest.html')
def reajax(req):
    if req.method=='POST':
        print(req.POST.get('username'))
        print(req.POST.get('password'))
        return HttpResponse('用户名或密码错误了')
    return HttpResponse('用户名.....')
def jsonp(request):
    return render(request, 'jsonp.html')
def logtest(request):
    return render(request, 'logtest.html')