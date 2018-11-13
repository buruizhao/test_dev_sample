from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm

# Create your views here.

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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name,describe=describe,status=status)

            return HttpResponseRedirect('/project/project_manage/')
    else:
        form = ProjectForm()

    return render(request, 'project_manage/project_manage.html', {
        'form': form,
        'type':'create'
    })

#跳转项目管理修改页面
@login_required
def project_manage_update(request,project_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            model = Project.objects.get(id=project_id)
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save()
            return HttpResponseRedirect('/project/project_manage/')
    else:
        if project_id:
            form = ProjectForm(
                instance = Project.objects.get(id=project_id)
            )

    return render(request, 'project_manage/project_manage.html', {
        'form': form,
        'type':'update',
        'project_id':project_id
    })

@login_required
def project_manage_delete(request,project_id):
    Project.objects.get(id=project_id).delete()
    return HttpResponseRedirect('/project/project_manage/')
