from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import ModuleForm

# Create your views here.

# 项目模块列表
@login_required
def project_module(request):
	username = request.session.get('user', '')  # 用session
	modules = Module.objects.order_by('-update_time')  # 查出项目模块，并按照更新时间倒序
	return render(request, 'project_module/project_module.html', {
		'user': username,
		'modules': modules,
		'type': 'list'
	})


# 跳转项目模块创建页面
@login_required
def project_module_create(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ModuleForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			project = form.cleaned_data['project']
			Module.objects.create(name=name, describe=describe, project=project)

			return HttpResponseRedirect('/project/project_module/')
	else:
		form = ModuleForm()

	return render(request, 'project_module/project_module.html', {
		'form': form,
		'type': 'create'
	})


# 跳转项目管理修改页面
@login_required
def project_module_update(request,module_id):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ModuleForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			model = Module.objects.get(id=module_id)
			model.name = form.cleaned_data['name']
			model.describe = form.cleaned_data['describe']
			model.project = form.cleaned_data['project']
			model.save()
			return HttpResponseRedirect('/project/project_module/')
	else:
		if module_id:
			form = ModuleForm(
				instance = Module.objects.get(id=module_id)
			)

	return render(request, 'project_module/project_module.html',{
		'form': form,
		'type':'update',
		'module_id':module_id
	})

@login_required
def project_module_delete(request,module_id):
	Module.objects.get(id=module_id).delete()
	return HttpResponseRedirect('/project/project_module/')
