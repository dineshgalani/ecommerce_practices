from django.shortcuts import render
from django.views.generic import ListView
from .models import Hr
# Create your views here.

class HrList(ListView):
    model = Hr
    hrlist = model.objects.all().values_list()
    print("list -->",Hr.objects.all())
    for i in Hr.objects.all():
        print(i.name)
        print(i.email)

    template_name = 'cbv/hr_list.html'
    context_oject_name = 'hrlist'