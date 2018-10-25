from django.contrib import admin

from product.models import Product, DailyPrice
from product.models import Channel
from product.models import Holding
from product.models import Waterbill

# Register your models here.
admin.site.register(Product)
admin.site.register(DailyPrice)
admin.site.register(Channel)
admin.site.register(Holding)
admin.site.register(Waterbill)