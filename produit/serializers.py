from rest_framework import serializers 
from .models import Produit , Category

class ProduitSerializer(serializers.ModelSerializer): 
    # To get name instead pk
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta: 
        model = Produit
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = "__all__"