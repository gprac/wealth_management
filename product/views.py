from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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
			#form.save()
			wb = form.save(False)
			pt = wb.product
			cl = wb.channel
			qs = Holding.objects.filter(product=pt, channel=cl)
			if len(qs)>0:
				hd = qs[0]
				if (wb.direction == 'B'):
					hd.volumes += wb.volumes
				else:
					hd.volumes -= wb.volumes
			else:
				hd=Holding()
				hd.product = pt
				hd.channel = cl
				hd.volumes = wb.volumes
			if hd.volumes > 0:
				hd.save()
				form.save()
			elif hd.volumes == 0:
				hd.delete()
				form.save()
			else:
				print("error")
			print(wb.product)
			return HttpResponseRedirect(reverse('product:index'))
		#products = Product.objects.all()
		#channels = Channel.objects.all()
		#print(channels)
	#context = {'products': products, 'channels':channels }
	context = {'form':form }
	return render(request, 'product/addwaterbill.html', context)