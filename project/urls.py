from django.contrib import admin
from django.urls import path , include
from hundelreactdj.views import front 
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('admin/', admin.site.urls), 
    path("produit_api/", include('produit.urls') ),
    path("cart/", include('cart.urls') ),
    path('create_post/' , include('createPost.urls') ),
    path('order/' , include('order.urls') ),
    path('payment/' , include('payment.urls') ),
    path('test_api/' , include('testApi.urls') ),
    path('auth/', include('rest_framework.urls')) ,
    #login using API
    path('rest-auth/', include('dj_rest_auth.urls')), 
    #Create Account using API 
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path("", front , name="front"), #Connect with default Route in React
    path('<path:route>/', front), #Connect with another route in React
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)