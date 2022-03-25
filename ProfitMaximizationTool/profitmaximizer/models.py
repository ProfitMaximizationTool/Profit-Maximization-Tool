from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class BusinessOwner(User):
	business_name = models.CharField(max_length=100)
	full_name = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return self.username

class IngredientRecord(models.Model):
	owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
	ingredient_name = models.CharField(max_length=255)
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.IntegerField()
	daily_units = models.IntegerField()

class ProductRecord(models.Model):
	owner = models.ForeignKey(BusinessOwner,on_delete=models.CASCADE)
	product_name = models.CharField(max_length=255)
	ingredients = models.JSONField(default=dict)
	cost = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

	def update_cost(self):
		new_cost = 0
		for ingr in self.ingredients.keys():
			try:
				target_ingr = IngredientRecord.objects.get(ingredient_name=ingr,owner=self.owner)
				new_cost += (target_ingr.cost)*(self.ingredients[ingr])
			except ObjectDoesNotExist:
				new_cost += 0
				
		self.cost = new_cost
		self.save()

class SalesRecord(models.Model):
	owner = models.ForeignKey(BusinessOwner,on_delete=models.CASCADE,null=True)
	date = models.DateField(null=True,unique=True)
	sales_report = models.JSONField(default=dict)
	profit = models.DecimalField(max_digits=10,decimal_places=2,default=0)

"""
suggestions for variable names
class ProductionRecord:
	date
	production_report
	expenses

class SalesRecord:
	date
	sales_report
	profit


"""