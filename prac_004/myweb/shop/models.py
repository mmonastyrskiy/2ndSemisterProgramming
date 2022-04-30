from django.db import models


class Brand(models.Model):
	self_id = models.IntegerField()
	Brand_name = models.CharField(max_length=100)
	description = models.TextField()



class Catalog(models.Model):
	id_parent = models.IntegerField()
	self_id = models.IntegerField()
	name = models.CharField(max_length=1000)
	text_html = models.TextField()


class Product(models.Model):
	self_id = models.IntegerField()
	arts = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	category = models.ForeignKey(Catalog, on_delete=models.CASCADE)
	link = models.CharField(max_length=1000)
	description = models.TextField()
class ProductPhoto(models.Model):
	product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
	filename = models.CharField(max_length=100)

# Create your models here.
