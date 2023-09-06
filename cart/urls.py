from django.urls import path
from . import views



urlpatterns = [
    path('add/<int:id>/<slug:slug>/<int:quantity>/', views.cart_add),
    path('update_quantity/<int:id>/<str:quantity>/' , views.cart_update_quantity ),
    path('remove/<int:id>/', views.cart_remove),
    path('details/' , views.cart_details ),
    path('clear/' , views.cart_clear),
    path('length/' , views.cart_length),  
]