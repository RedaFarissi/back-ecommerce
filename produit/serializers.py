from rest_framework import serializers 
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer): 
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta: 
        model = Produit
        fields = "__all__"