from rest_framework import serializers 
from .models import Store

class StoreSerializer(serializers.ModelSerializer): 
    image = serializers.ImageField(required=True)
    class Meta:
        model = Store
        fields = "__all__"