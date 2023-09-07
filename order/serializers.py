from rest_framework import serializers
from .models import Order , OrderItem
from produit.models import Produit

class OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Order
        fields = "__all__"


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('image',)  


class OrderItemSerializer(serializers.ModelSerializer):
    product_info = ProduitSerializer(source='product', read_only=True)
    class Meta: 
        model = OrderItem
        fields = "__all__"