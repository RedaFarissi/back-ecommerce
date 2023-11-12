from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from django.shortcuts import  get_object_or_404
from produit.models import Produit
from produit.serializers import ProduitSerializer
from rest_framework.permissions import AllowAny





@api_view(["GET"])
@permission_classes([AllowAny])
def cart_add(request, id, slug, quantity):
    #get the session cart or create empty dictionary 
    cart = request.session.get('cart' , {})
    
    product = get_object_or_404(Produit, id=id, slug=slug)

    cart[str(id)] = {
        "id" :id , 
        "product": ProduitSerializer(product).data , 
        "quantity": quantity , 
        "image_url": request.build_absolute_uri(product.image.url) if product.image else None,
    }
    
    # Save the modified cart in the session
    request.session["cart"] = cart
    return Response({"cart": True })


@api_view(['GET'])
def cart_update_quantity(request, id , quantity ):
    cart = request.session.get('cart' , {})
    
    if str(id) in cart:
        cart[str(id)]['quantity'] = quantity 

    # Save the modified cart in the session
    request.session["cart"] = cart
    
    return Response({"cart": True})

@api_view(['GET'])
@permission_classes([AllowAny])
def cart_remove(request, id):
    cart = request.session.get('cart' , {})
    if str(id) in cart:
        del cart[str(id)]
    # Save the modified cart in the session
    request.session["cart"] = cart
    return Response({"cart": True})

@api_view(['GET'])
def cart_details(request):
    cart = request.session.get('cart' , {})
    length = len(cart.keys())
    return Response({"cart": cart , "length":length})

@api_view(['GET'])
def cart_clear(request):
    if 'cart' in request.session :
        del request.session['cart']
    return Response({"cart":True})

@api_view(['GET'])
def cart_length(request):
    cart = request.session.get('cart' , {})
    length = len(cart.keys())
    return Response({"length": length})
