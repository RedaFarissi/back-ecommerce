from django.urls import path
from . import views 

urlpatterns = [ 
    path('' , views.add_some_product_from_api_to_database ),  
    path('check_if_admin/' , views.check_if_admin ),  
] 