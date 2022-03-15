from asyncio.windows_events import NULL
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

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
	productName = models.CharField(max_length=255)
	ingredients = models.JSONField(default=dict)
	cost = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	price = models.DecimalField(max_digits=10,decimal_places=2)

	def update_cost(self):
		new_cost = 0
		for ingr in self.ingredients.keys():
			for irecord in IngredientRecord.objects.all():
				if irecord.owner == self.owner and ingr == irecord.ingredient_name:
					new_cost += (irecord.cost)*(self.ingredients[ingr])
		self.cost = new_cost
		self.save()
		