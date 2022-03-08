from http.client import HTTPMessage
from importlib.resources import contents
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from .models import employee1


# Create your views here.

def group(request):
    context = {
        'name':'Dinesh'
    }
    return render(request,'group/index.html',context)

def add(request):
    return HttpResponse("hello this is add call...")

def contactUs(request):
    context = {
        'contact_name' : ['rajesh','suresh','dinesh','arjun','paresh'],
    }
    return render(request,'group/contactUs.html',context)

def aboutus(request):
    context = {
        'isActive': True,
        'age' : 20
    }
    return render(request,'group/aboutus.html',context)

def addEmployee(request):
    emp = employee1(ename='john',eemail='john@123',econtact=9099179363,eage=24)
    emp.save()
    return HttpResponse("employee added....")

def viewEmployee(request):
    employees = employee1.objects.all().values_list()   
    print(employees)
    return render(request,'group/view.html',{'employees':employees})

def deleteEmployee(request):
    emp = employee1.objects.all()
    emp.delete()
    return HttpResponse('Employees deleted')

def updateEmployee(request):
    emp = employee1.objects.get(id = 35)
    emp.eage = 30
    emp.ename = 'dinesh' 
    emp.save()
    return HttpResponse('Employee updated')