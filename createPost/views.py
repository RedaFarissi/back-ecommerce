from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from produit.models import Produit , Category
from produit.serializers import ProduitSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.utils.text import slugify 
from rest_framework import status
from rest_framework.exceptions import ValidationError

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def products_created_by_user(request):
    products = Produit.objects.filter(author=request.user)
    return Response({"produits_user": ProduitSerializer(products, many=True , context={'request': request}).data}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_delete(request,id,slug):
    product = Produit.objects.get(id=id , slug=slug)
    product.delete()
    return Response({"product_delete": True })

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    parser_classes = (MultiPartParser, FormParser)
    data = request.data
    category_name = data['category']
    category = Category.objects.get(name=category_name).id
    data['category'] = category
    data['slug'] = slugify(data['title'])
    data['author'] = User.objects.get(username=request.user).id
    data['available'] = True
    
    serializer = ProduitSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
    try:
        serializer.is_valid(raise_exception=True)  # Raise exception on validation error
    except ValidationError as e:
        print("Validation error: ", e)
        return Response({"msg": "Validation failed"}, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response({"msg": True}, status=status.HTTP_201_CREATED)