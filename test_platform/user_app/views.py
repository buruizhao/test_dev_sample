from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

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
                auth.login(request,user)
                return render(request, "project_manage.html")
            else:
                return render(request, 'index.html', {'error': '用户名或密码错误，请重新登录！'})
