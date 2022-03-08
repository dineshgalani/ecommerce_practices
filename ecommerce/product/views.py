from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def addProduct(request):
    return HttpResponse("ADD Product Called...")

#create viewProduct fuction to Display product page

def viewProduct(request):
    return HttpResponse("viewProduct Called....")

#create productpage functoion to show probuct page via html

def productpage(request):
    return render(request,'product/productpage.html')

#creat contac us html page render 

def contactus(request):
    return render(request,'product/contactus.html')

#creat contac us html page render 

def aboutus(request):
    return render(request,'product/aboutus.html')

#creat two buttons and render in prodect page

def button3(request):
    return render(request,'product/button3.html')

def button4(request):
    return render(request,'product/button4.html')