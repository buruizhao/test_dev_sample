from django.shortcuts import render
from project_app.models import Module
from django.contrib.auth.decorators import login_required

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