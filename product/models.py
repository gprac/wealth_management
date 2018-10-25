from django.db import models

# Create your models here.
class Product(models.Model):
	code = models.CharField(max_length=200)
	name = models.CharField(max_length=999)
	TYPE_CHOICES = (
        (u'F', u'Fund'),
        (u'S', u'Stock'),
    )
	type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	def __str__(self):
		return self.name

		
		
class DailyPrice(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
	price = models.FloatField()
	date = models.DateTimeField()




class Channel(models.Model):
	name = models.CharField(max_length = 999)
	def __str__(self):
		return self.name

class Holding(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
	volumes = models.FloatField()
	channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
	def __str__(self):
		return str(self.product)+'\t'+str(self.volumes)+'\t'+str(self.channel)


class Waterbill(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
	channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)	
	DIRECTION_CHOICE = (
		(u'B', u'Buy'),
		(u'S', u'Sell'),
	)
	
	direction = models.CharField(max_length=100, choices = DIRECTION_CHOICE)
	volumes = models.FloatField()
	price = models.FloatField()
	add_date = models.DateTimeField()