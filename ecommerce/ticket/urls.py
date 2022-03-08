from django.urls import include, path
from .views import CreateTicket

urlpatterns = [
    path('add/',CreateTicket.as_view())
]