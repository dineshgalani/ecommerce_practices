from django.http import request
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import task
from django.views.generic import DetailView

class CreateTask(CreateView):
    model = task
    fields = ['task_name','task_description']
    template_name = 'task/create_task.html'
    success_url = '/task/view/'
    

class DeleteTask(DeleteView):
    model = task
    success_url= 'task/view/'


def index(request):
    return render(request, 'task/index.html')

class UpdateTask(UpdateView):
    model = task
    fields = ['task_name', 'task_description']
    template_name = 'task/update_task.html'
    success_url = '/task/view/'

class TaskDetail(DetailView):
    model = task
    template_name = 'task/task_detail.html'    