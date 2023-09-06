from rest_framework import serializers 
from .models import Produit , Category , Like

class ProduitSerializer(serializers.ModelSerializer): 
    # To get name instead pk
    category_name = serializers.ReadOnlyField(source='category.name')
    total_likes = serializers.SerializerMethodField()
    class Meta: 
        model = Produit
        fields = "__all__"
    
    def get_total_likes(self, obj):
        return obj.total_likes()

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = "__all__"

