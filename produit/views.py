from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Produit , Category
from .serializers import ProduitSerializer , CategorySerializer


@api_view(['GET'])
def index(request ) :
    allProduct = Produit.objects.all()
    allCategory = Category.objects.all()
    bestDiscount = Produit.objects.raw('''SELECT id , ( %s - (price_reduction * %s / default_price)) AS porsontage FROM produit_produit ORDER BY(porsontage) DESC LIMIT 4''',[100,100])
    lastFourProduit = Produit.objects.all().order_by('-id')[:4]
    startFiveLastFour = Produit.objects.filter(start=Produit.GenereChoicesStart.five).order_by('-id')[:4]
    dealOfDay = Produit.objects.raw('SELECT id , ( %s - (price_reduction * %s / default_price)) AS porsontage  FROM produit_produit ORDER BY(porsontage) DESC',[100,100])[:2]
    lastProduitAfterFour = Produit.objects.raw('SELECT * FROM produit_produit WHERE id < (SELECT COUNT(id) - %s FROM produit_produit) ORDER BY id DESC',[3])[:8]
    
    # if category_slug:
    #     category = Category.objects.get(slug=category_slug)
    #     allProduct = Produit.objects.filter(category=category)

    #context={'request': request} :  is use to can get the data from media in front.
    content = {
        'all_product': ProduitSerializer(allProduct, many=True , context={'request': request}).data ,
        'all_category': CategorySerializer(allCategory , many=True).data  ,  
        'best_discount': ProduitSerializer(bestDiscount, many=True , context={'request': request}).data ,
        'last_four_produit': ProduitSerializer(lastFourProduit, many=True ,context={'request': request}).data ,
        'start_five_last_four': ProduitSerializer(startFiveLastFour, many=True , context={'request': request}).data ,
        'deal_of_day' : ProduitSerializer(dealOfDay, many=True , context={'request': request}).data ,
        'last_produit_after_four' : ProduitSerializer(lastProduitAfterFour, many=True , context={'request': request} ).data ,
    } 
    return Response(content)

@api_view(['GET'])
def detail(request , category_slug=None) :
    category = Category.objects.get(slug=category_slug)
    allProduct = Produit.objects.filter(category=category)
    return Response({
        'all_product':ProduitSerializer(allProduct ,many=True , context={'request': request}).data ,
    })