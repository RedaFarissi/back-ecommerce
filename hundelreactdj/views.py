from django.shortcuts import render

# Create your views here.
def front(request , route=None):
   return render(request, "index.html")