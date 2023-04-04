from rest_framework import generics
from .models import Store
from .serializers import StoreSerializer
from rest_framework.authentication import TokenAuthentication

class AddStore(generics.CreateAPIView):
    #authentication_classes is for check for key Token 
    authentication_classes = [TokenAuthentication]
    model = Store
    serializer_class = StoreSerializer