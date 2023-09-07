from django.urls import path 
from . import views

urlpatterns = [
    path('create/', views.create_payment ) ,
    path('success_payment/', views.success_payment ) ,
    path('last_order_item/', views.last_order_item)
]