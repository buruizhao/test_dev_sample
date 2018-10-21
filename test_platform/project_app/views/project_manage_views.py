from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm

# Create your views here.

def project_manage_forms(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()

    return render(request, '/project/project_manage/', {'form': form})


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
