from django.urls import path
from product import views

urlpatterns = [

    path('addProduct/',views.addProduct),
    path('viewProduct/',views.viewProduct), 
    path('productpage/',views.productpage), 
    path('productpage/contactus/',views.contactus),
    path('productpage/aboutus/',views.aboutus),
    path('productpage/button3/',views.button3),
    path('productpage/button4/',views.button4),
]
