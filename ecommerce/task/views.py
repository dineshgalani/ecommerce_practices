from dataclasses import field
from sre_constants import SUCCESS
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import task
from django.views.generic import CreateView

# Create your views here.

class createTask(CreateView):
    model = task
    field = ['task_name','task_desctption']
    tamplate_name = 'task/create.html'
    success_url = '/task/view'