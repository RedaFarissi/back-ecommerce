from django.urls import path
from . import views 

urlpatterns = [ 
    path('create/' , views.create_post ),
    path('products_created_by_user/' , views.products_created_by_user ),
    path('product_delete/<int:id>/<slug:slug>/' , views.product_delete ),
] 