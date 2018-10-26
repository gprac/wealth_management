from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Holding, Product, Channel, DailyPrice
from .forms import WaterbillForm

import json
# Create your views here.


class shizhi:
	def __init__(self, holding, dailyprice):
		self.holding = holding
		self.dp = dailyprice
		self.mv = holding.volumes * dailyprice

	def __str__(self):
		return str(self.holding.product)+'\t'+ str(self.holding.volumes)+'\t净值:'+str(self.dp)+'\t市值:'+str(self.mv)	


def index(request):
	holdings = Holding.objects.all()
	#context = { 'holdings':holdings }
	total = 0
	allholdingsz =[]
	piedatalist = []
	for holding in holdings:
		dp = DailyPrice.objects.filter(product=holding.product).order_by('date')
		sz = shizhi(holding, dp[0].price)
		allholdingsz.append(sz)
		piedatalist.append({'value':sz.mv, 'name':str(holding.product)})
		print(piedatalist)
		total = total + sz.mv
	context = { 'allholdingsz':allholdingsz , 'total' : total, 'piedatalist':json.dumps(piedatalist)}
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