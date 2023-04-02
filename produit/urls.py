from django.urls import path
from . import views 

urlpatterns = [ 
    #جميع المنتجات 
    path('', views.AllProfileAPIView.as_view()), 
    #أحسن تخفيضات 
    path('best_discount/', views.BestDiscountAPIView.as_view()), 
    #أخر المنتجات 
    path('last_four_produit/' , views.LastFourProduitAPIView.as_view()),
    #الأعلى تقييما 
    path('start_five_last_four/', views.StartFiveLastFourAPIView.as_view()),
    #صفقة اليوم 
    path('deal_of_day/' , views.DealOfDayAPIView.as_view()),
    #منتجات جديدة
    path('last_produit_after_four/' , views.LastProduitAfterFourAPIView.as_view()),
    path('category/<str:name>/' , views.EachCategoryAPIView.as_view()),
] 