from rest_framework import generics
from .models import Store
from .serializers import StoreSerializer


class AddStore(generics.CreateAPIView):
    model = Store
    serializer_class = StoreSerializer