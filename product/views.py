from django.shortcuts import render

from .models import Holding, Product, Channel
from .forms import WaterbillForm

# Create your views here.

def index(request):
	holdings = Holding.objects.all()
	context = { 'holdings':holdings }
	return render(request, 'product/index.html', context)
	
def addwaterbill(request):
	if request.method != 'POST':
		form = WaterbillForm()
	else:
		form = WaterbillForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('product:index'))
		#products = Product.objects.all()
		#channels = Channel.objects.all()
		#print(channels)
	#context = {'products': products, 'channels':channels }
	context = {'form':form }
	return render(request, 'product/addwaterbill.html', context)