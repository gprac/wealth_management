from django.shortcuts import render

from .models import Holding, Product, Channel

# Create your views here.

def index(request):
	holdings = Holding.objects.all()
	context = { 'holdings':holdings }
	return render(request, 'product/index.html', context)
	
def addwaterbill(request):
	products = Product.objects.all()
	channels = Channel.objects.all()
	print(channels)
	context = {'products': products, 'channels':channels }
	return render(request, 'product/addwaterbill.html', context)