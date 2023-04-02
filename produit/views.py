from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Produit , Category
from .serializers import ProduitSerializer


def front(request):   
   return render(request, "index.html")

# جميع المنتجات
class AllProfileAPIView(generics.ListAPIView): 
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
# أحسن تخفيضات  
class BestDiscountAPIView(generics.ListAPIView): 
    queryset = Produit.objects.raw('''SELECT id , ( %s - (price_reduction * %s / default_price)) AS porsontage  
                                   FROM produit_produit ORDER BY(porsontage) DESC LIMIT 4''',[100,100])
    serializer_class = ProduitSerializer

# أخر المنتجات 
class LastFourProduitAPIView(generics.ListAPIView): 
    queryset = Produit.objects.all().order_by('-id')[:4]
    serializer_class = ProduitSerializer

# الأعلى تقييما 
class StartFiveLastFourAPIView(generics.ListAPIView):
    queryset = Produit.objects.filter(start=Produit.GenereChoicesStart.five).order_by('-id')[:4]
    serializer_class = ProduitSerializer

# صفقة اليوم 
class DealOfDayAPIView(generics.ListAPIView):
    queryset = Produit.objects.raw('SELECT id , ( %s - (price_reduction * %s / default_price)) AS porsontage  FROM produit_produit ORDER BY(porsontage) DESC',[100,100])[:2]
    serializer_class = ProduitSerializer

# منتجات جديدة
class LastProduitAfterFourAPIView(generics.ListAPIView):  
    queryset = Produit.objects.raw('SELECT * FROM produit_produit WHERE id < (SELECT COUNT(id) - %s FROM produit_produit) ORDER BY id DESC',[3])[:8]
    serializer_class = ProduitSerializer 
    
# each Category
class EachCategoryAPIView(generics.ListAPIView):  
    serializer_class =  ProduitSerializer
    def get(self,request,name):  
        category_name = Category.objects.get(name=name)
        type_content = Produit.objects.filter(category=category_name)
        queryset = type_content.values('id','image','title','description','start','default_price','price_reduction','the_number_of_pieces','Offer_ends_after',)
        return Response({'products': queryset})