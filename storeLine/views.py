from rest_framework import generics 
from .models import Store
from .serializers import StoreSerializer
from rest_framework.permissions import IsAuthenticated

#from rest_framework.authentication import TokenAuthentication

from rest_framework.parsers import MultiPartParser

class AddStore(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    #authentication_classes = [TokenAuthentication]
    model = Store
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    parser_classes = [MultiPartParser] # to apload image 

    def perform_create(self, serializer):
        print("perform_create")
        serializer.save(author=self.request.user)

