from django.shortcuts import render

from .models import Products_db

# Create your views here.
def index(request):
    all_products = Products_db.objects.all()
    return render(request,'products/index.html',{'all_products':all_products})

