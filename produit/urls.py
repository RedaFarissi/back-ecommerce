from django.urls import path
from . import views 

urlpatterns = [ 
    path('' , views.index ),
    path('<slug:category_slug>/' , views.detail ),
] 