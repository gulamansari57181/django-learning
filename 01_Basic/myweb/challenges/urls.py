# To create urls we create urlpatterns list and values inside the list is path()-> to specific view
from django.urls import path
# importing from same folder following syntax is used
from . import views

urlpatterns = [
    
    path("",views.index),
    path("<str:month>", views.monthly_challenge,name="month-name")

]
