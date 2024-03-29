from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes 
from rest_framework.permissions import AllowAny 
from produit.models import Produit
from .models import OrderItem
from .serializers import OrderSerializer


@api_view(['POST'])
@permission_classes([AllowAny]) 
def order_create(request):
    cart = request.session.get('cart',{})
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        # Save the validated data as a new Order instance
        order = serializer.save()
        for cart_item in cart.values():
            product = cart_item['product']
            price_reduction = product['price_reduction']
            quantity = cart_item['quantity']
            product_instance = Produit.objects.get(id=product['id'])
            OrderItem.objects.create(
                order=order, 
                product=product_instance, 
                price=price_reduction, 
                quantity=quantity
            )
            
        if 'cart' in request.session :
            del request.session['cart']
        return Response({'cart_data': 'Order created successfully'})
    else:
        return Response({"error":"Order Create Error"})