from django.contrib import admin
from .models import Employee,Role, customer, order, product, student
# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(student)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(product)
