from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Project,Module

# Create your views here.

#登陆首页
# def index(request):
#     return HttpResponse("Hello world！")

def index(request):
    return render(request,"index.html")

#登陆逻辑处理
def login_action(request):
    # if request.method == 'GET':
    #     username = request.GET.get('username','')
    #     password = request.GET.get('password','')

    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        if username == '' or password == '':
            return render(request, 'index.html', {'error':'用户名或密码不能为空，请重新登录！'})
        else:
            user = auth.authenticate(username = username,password = password)

            # if username == 'admin' and password == '123456':

            if user is not None:
                auth.login(request,user) #记录用户登录状态
                # return render(request, "project_manage.html", {'user':user}) #普通返回
                request.session['user'] = username  # 用session替换cookie
                response = HttpResponseRedirect('/project_manage/')
                # response.set_cookie('user', username, 3600) #添加浏览器cookie
                return response
            else:
                return render(request, 'index.html', {'error': '用户名或密码错误，请重新登录！'})

#项目管理页面
@login_required #判断用是否登录
def project_manage(request):
    # username = request.COOKIES.get('user','') #读取浏览器的cookie
    username = request.session.get('user','') #用session替换cookie
    projects = Project.objects.order_by('-update_time') #查出项目，并按照更新时间倒序
    return render(request, 'project_manage.html',
                  {'user':username,
                   'projects':projects
                }
    )

#退出登录
@login_required
def logout(request):
    auth.logout(request) #清除用户的登陆状态
    return HttpResponseRedirect('/')