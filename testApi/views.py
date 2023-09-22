from rest_framework.response import Response
from django.http import JsonResponse
from produit.models import Produit, Category 
from .product_api import  products_api 
from django.utils.text import slugify
import os
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from produit.serializers import ProduitSerializer , CategorySerializer
from rest_framework.permissions import IsAdminUser , AllowAny
from rest_framework.authentication import TokenAuthentication

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def add_some_product_from_api_to_database(request):    
    for product_data in products_api :    
        # Create the category instance if not exist
        category, _ = Category.objects.get_or_create(
            slug=slugify(product_data['category']),
            defaults={'name': product_data['category']}
        )   

        #create instence from Category used
        check_category = Category.objects.get(name=product_data['category'])
       
        product, created = Produit.objects.get_or_create(
            title=product_data['title'],
            author=request.user,
            defaults={
                'category': check_category,
                'slug': slugify(product_data['title']),
                'description': product_data['description'],
                'price_reduction': product_data['price'],
                'default_price':product_data['default_price'],
                'start':product_data['start'],
                'description':f"{product_data['title']} bla bla bla" ,
            }
        )
    return JsonResponse({"msg":"Data added"})
        

from django.contrib.auth.models import User

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def check_if_admin(request):
    return JsonResponse({"is_admin":True})