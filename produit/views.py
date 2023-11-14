from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from .models import Produit , Category , Like
from .serializers import ProduitSerializer , CategorySerializer 
from django.shortcuts import get_object_or_404 
# from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Q
from datetime import  date




@api_view(['GET'])
@authentication_classes([TokenAuthentication]) 
@permission_classes([AllowAny])
def index(request):
    #get date to last product created 
    last_product_query = Produit.objects.latest('created_at')
    last_product_date = last_product_query.created_at
    year = last_product_date.year
    month = last_product_date.month
    day = last_product_date.day
    target_date = date(year, month, day)
    print(target_date)

    #produit_produit === appName__tableName

    allProduct = Produit.objects.filter(available=True).order_by('-id')
    allCategory = Category.objects.all()
    bestDiscount = Produit.objects.raw('''SELECT 
            id , 
            ( %s - (price_reduction * %s / default_price)) AS porsontage 
        FROM produit_produit 
        WHERE available=TRUE 
        ORDER BY porsontage  DESC 
        LIMIT 8''',[100,100])
    lastFourProduit = Produit.objects.all().order_by('-id')[:4]
    startFiveLastFour = Produit.objects.filter(start=Produit.GenereChoicesStart.five).order_by('-id')[:4]
    
    
    dealOfDay = Produit.objects.filter(created_at__date=target_date).extra(
        select={
            'percentage': '%s - (price_reduction * %s / default_price)'
        },
        select_params=[100, 100]
    ).order_by('-percentage')[:2]
    
    lastProduitAfterFour = Produit.objects.raw('SELECT * FROM produit_produit WHERE id < (SELECT COUNT(id) - %s FROM produit_produit) ORDER BY id DESC',[3])[:8]
    top_4_products_has_liked = Produit.objects.filter(available=True).annotate(like_count=Count('like')).order_by('-like_count')[:4]
    

    content = {
        'all_product': ProduitSerializer(allProduct, many=True , context={'request': request}).data ,
        'all_category': CategorySerializer(allCategory , many=True).data  ,  
        'best_discount': ProduitSerializer(bestDiscount, many=True , context={'request': request}).data ,
        'last_four_produit': ProduitSerializer(lastFourProduit, many=True ,context={'request': request}).data ,
        'start_five_last_four': ProduitSerializer(startFiveLastFour, many=True , context={'request': request}).data ,
        'deal_of_day' : ProduitSerializer(dealOfDay, many=True , context={'request': request}).data ,
        'last_produit_after_four' : ProduitSerializer(lastProduitAfterFour, many=True , context={'request': request} ).data ,
        'top_4_products_has_liked':ProduitSerializer(top_4_products_has_liked, many=True , context={'request': request} ).data ,
    } 
    return Response(content)

@api_view(['GET'])
def products_by_category(request , category_slug=None) :
    category = Category.objects.get(slug=category_slug)
    allProduct = Produit.objects.filter(category=category)
    return Response({
        'all_product':ProduitSerializer(allProduct ,many=True , context={'request': request}).data ,
    })


@api_view(['GET'])
def product_detail(request ,  slug):
    produit = get_object_or_404(Produit, slug=slug )
    return Response({'product_detail':ProduitSerializer(produit , context={'request': request}).data , })



@api_view(['POST'])
@authentication_classes([TokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def add_like(request , id ,slug):    
    produit = get_object_or_404( Produit, id=id , slug=slug ) 

    #ckeck if user add like or not if yes delete this from Like models
    if Like.objects.filter(user=request.user, produit=produit).exists():
        like = Like.objects.filter(user=request.user, produit=produit).delete()
        return Response({"like":False})
  
    like = Like(user=request.user, produit=produit)
    like.save()
    
    return Response({"like":True})


@api_view(["GET"])
@authentication_classes([TokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
def product_liked(request, product_id):
    product = Produit.objects.get(id=product_id)
    like = Like.objects.filter(user=request.user, produit=product).exists()
    return Response({"is_like": like})


@api_view(["POST","GET"])
@authentication_classes([TokenAuthentication]) 
@permission_classes([AllowAny]) 
def search_feature(request):
    if request.method == "POST":
        search = request.POST.get('search', '')
        search = Produit.objects.filter(title__icontains=search)
        return Response({"search": ProduitSerializer(search ,many=True , context={'request': request}).data })
    else:
        return Response({"search": False })