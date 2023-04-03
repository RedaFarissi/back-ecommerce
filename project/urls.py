from django.contrib import admin
from django.urls import path , include
from hundelreactdj.views import front 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", front , name="front"),
    
    path("produit_api/", include('produit.urls') ),
    path("store/", include('storeLine.urls') ),
    
    path('auth/', include('rest_framework.urls')) ,
    path('rest-auth/', include('dj_rest_auth.urls')), #new
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)