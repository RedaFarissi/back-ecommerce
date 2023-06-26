from rest_framework import generics 
from django.http import  HttpResponse
from .models import Store
from .serializers import StoreSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from rest_framework.parsers import MultiPartParser , FormParser

from django.contrib.auth.models import User



class AddStore(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    model = Store
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    parser_classes = (MultiPartParser , FormParser ) # to apload image 

    def post(self, request, *args, **kwargs):
        data = request.data
        data['author'] = User.objects.get(username=self.request.user).id
        serializer = StoreSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"message": "CREATE SUCCESS"}, status=201)
        return HttpResponse({"error": "error in code"}, status=400)