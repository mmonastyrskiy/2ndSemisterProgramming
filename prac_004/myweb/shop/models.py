from django.db import models

# Create your models here.
class Product(models.Model):
	#Product_id = models.IntegerField()
	Product_art = models.CharField(max_length = 1000)
	Product_name = models.CharField(max_length= 1000)
	Product_price = models.CharField(max_length=1000)
	Product_brand = models.CharField(max_length= 1000)
	Product_category = models.CharField(max_length = 1000)
	Product_origin_link = models.CharField(max_length = 1000)
	Product_description = models.TextField()