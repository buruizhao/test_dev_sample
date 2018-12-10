from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

#登陆首页
# def index(request):
#     return HttpResponse("Hello world！")

def index(request):
    return render(request,"index.html")

#登陆逻辑处理
def login_action(request):

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
                response = HttpResponseRedirect('/project/project_manage/')
                # response.set_cookie('user', username, 3600) #添加浏览器cookie
                return response
            else:
                return render(request, 'index.html', {'error': '用户名或密码错误，请重新登录！'})


    else:
        return render(request, 'index.html')


#退出登录
@login_required
def logout(request):
    auth.logout(request) #清除用户的登陆状态
    return HttpResponseRedirect('/')