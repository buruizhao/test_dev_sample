from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#登陆首页
# def index(request):
#     return HttpResponse("Hello world！")

def index(request):
    return render(request,"index.html")

#登陆逻辑处理
def login_action(request):
    if request.method == 'GET':
        username = request.GET.get('username','')
        password = request.GET.get('password','')

        if username == '' and password == '':
            return render(request, 'index.html', {'error':'用户名或密码不能为空，请重新登录！'})

        if username == 'admin' and password == 'admin':
            return HttpResponse('登陆成功')
        else:
            return render(request, 'index.html', {'error':'用户名或密码错误，请重新登录！'})