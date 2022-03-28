from enum import unique
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
	ingredient_name = models.CharField(max_length=255,unique=True)
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	units = models.IntegerField()
	daily_units = models.IntegerField()

class ProductRecord(models.Model):
	owner = models.ForeignKey(BusinessOwner,on_delete=models.CASCADE)
	product_name = models.CharField(max_length=255,unique=True)
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
	revenue = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	profit = models.DecimalField(max_digits=10,decimal_places=2,default=0)

	def update_revenue(self):
		new_revenue = 0
		for prod in self.sales_report.keys():
			try:
				target_prod = ProductRecord.objects.get(product_name=prod,owner=self.owner)
				new_revenue += (target_prod.price)*(self.sales_report[prod])
			except ObjectDoesNotExist:
				revenue += 0
		self.revenue = new_revenue
		self.save()

	def update_profit(self):
		new_profit = 0
		try:
			target_day = ProductionRecord.objects.get(date=self.date,owner=self.owner)
			new_profit = self.revenue - target_day.expenses
		except ObjectDoesNotExist:
			new_profit += 0
		self.profit = new_profit
		self.save()

class ProductionRecord(models.Model):
	owner = models.ForeignKey(BusinessOwner,on_delete=models.CASCADE,null=True)
	date = models.DateField(null=True,unique=True)
	production_report = models.JSONField(default=dict)
	expenses = models.DecimalField(max_digits=10,decimal_places=2,default=0)

	def update_expenses(self):
		new_expense = 0
		for prod in self.production_report.keys():
			try:
				target_prod = ProductRecord.objects.get(product_name=prod, owner=self.owner)
				new_expense += (target_prod.cost)*(self.production_report[prod])
			except ObjectDoesNotExist:
				expenses += 0
		self.expenses = new_expense
		self.save()
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