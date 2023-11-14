from django.urls import path
from . import views 

urlpatterns = [ 
    path('' , views.index ),
    path('product/<slug:slug>/' , views.product_detail),
    path('product_liked/<int:product_id>/' , views.product_liked ),
    path('search/' , views.search_feature ),    
    path('<slug:category_slug>/' , views.products_by_category ),
    path('add_like/<int:id>/<slug:slug>/' , views.add_like ),
] 