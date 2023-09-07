from django.shortcuts import redirect
from django.conf import settings
import paypalrestsdk
from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from order.models import OrderItem , Order
from order.serializers import OrderItemSerializer
from django.db.models import Max



paypalrestsdk.configure({
    "mode": "sandbox", # Use "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID ,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def last_order_item(request):
    latest_order_id = OrderItem.objects.aggregate(Max('order_id'))['order_id__max']
    # Then, retrieve all products associated with that order ID
    latest_order_products = OrderItem.objects.filter(order_id=latest_order_id).select_related('product')
    return JsonResponse({"last_order_item": OrderItemSerializer(latest_order_products, many=True , context={'request': request}).data })

@api_view(["POST"])
@permission_classes([AllowAny])
def create_payment(request):
    # First, get the latest order ID
    latest_order_id = OrderItem.objects.aggregate(Max('order_id'))['order_id__max']
    # Then, retrieve all products associated with that order ID
    latest_order_products = OrderItem.objects.filter(order_id=latest_order_id).select_related('product')
    
    amount = 0
    for i in latest_order_products :
        amount =+ amount + i.get_cost()
    
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:3000/success_page/",
            "cancel_url": "http://localhost:3000/error_page/"
        },
        "transactions": [{
            "amount": {
                "total": str(amount),
                "currency": "USD"
            },
            "description": "This is a test transaction."
        }]
    })

    if payment.create():
        # Extract the PayPal approval URL from the payment response
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = link.href   
                return JsonResponse({"redirect_url": redirect_url})
    else:
        # Handle payment creation errors
        return JsonResponse({"error": str(payment.error)}, status=400)
    
@api_view(["GET"])
@permission_classes([AllowAny])
def success_payment(request):
    latest_order_id = OrderItem.objects.aggregate(Max('order_id'))['order_id__max']
    # Create or retrieve the order based on the latest_order_id
    order, created = Order.objects.get_or_create(id=latest_order_id)
    # Mark the order as paid
    order.paid = True
    order.save()
    return JsonResponse({"redirect_url": "Paid Successful"})
    