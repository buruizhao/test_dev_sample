from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import Project,Module

# Create your views here.

#项目管理：

#项目管理列表
@login_required #判断用是否登录
def project_manage(request):
    # username = request.COOKIES.get('user','') #读取浏览器的cookie
    username = request.session.get('user','') #用session替换cookie
    projects = Project.objects.order_by('-update_time') #查出项目，并按照更新时间倒序
    return render(request, 'project_manage/project_manage.html', {
	    'user':username,
        'projects':projects,
        'type':'list'
    })

#跳转项目管理创建页面
@login_required
def project_manage_create(request):
	return render(request, 'project_manage/project_manage.html', {
	    'type':'create'
    })

#跳转项目管理修改页面
@login_required
def project_manage_update(request):
    return render(request, 'project_manage/project_manage.html', {
	    'type': 'update'
    })

#项目管理删除操作
@login_required
def project_manage_delete(request):
	return render(request, 'project_manage/project_manage.html', {
		'type': 'delete'
	})

#############################################################################
#项目模块：

#项目模块列表
@login_required
def project_module(request):
    username = request.session.get('user', '')  # 用session
    modules = Module.objects.order_by('-update_time') #查出项目模块，并按照更新时间倒序
    return render(request, 'project_module/project_module.html',
                  {
                      'user':username,
                      'modules':modules,
	                  'type': 'list'
                  }

    )

#跳转项目模块创建页面
@login_required
def project_module_create(request):
    return render(request, 'project_module/project_module.html', {
	    'type':'create'
    })

#跳转项目管理修改页面
@login_required
def project_module_update(request):
    return render(request, 'project_module/project_module.html', {
	    'type': 'update'
    })