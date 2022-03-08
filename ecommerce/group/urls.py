
from operator import concat
from django.urls import include, path
from group import views

urlpatterns = [
 
   path('',views.group),
   path('contactus/',views.contactUs),
   path('add/',views.add),
   path('aboutus/',views.aboutus),
   path('addEmployee/',views.addEmployee),
   path('viewEmployee/',views.viewEmployee),
   path('deleteEmployee/',views.deleteEmployee),
   path('updateEmployee/',views.updateEmployee)

]
