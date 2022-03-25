from decimal import Decimal
from distutils import core
from multiprocessing import context
from tkinter.tix import AUTO
from turtle import update
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from profitmaximizer.models import BusinessOwner, IngredientRecord, ProductRecord, SalesRecord
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from profitmaximizer.utils import update_all_products
import json
from datetime import datetime

def index_view(request):
	# default loading of index page
	return render(request, "index.html",  context={"auth_error": "none"})

@csrf_protect
def signup_view(request):
	# make sure the request came from the sign up form
	if request.method == "POST" and "signup-btn" in request.POST:
		if request.POST['psw'] == request.POST['confirmpsw']: # confirmed password
			full_name = request.POST['fullname']
			username = request.POST['username']
			password = request.POST['psw']
			business_name = request.POST['bizname']

			try: # username already taken
				business_owner = BusinessOwner.objects.get(username=username)
				return render(request, "index.html", context={"auth_error": "username taken"})

			except ObjectDoesNotExist: # valid username
				business_owner = BusinessOwner.objects.create_user(username=username, email=None, password=password)
				business_owner.business_name = business_name
				business_owner.full_name = full_name
				business_owner.save()
				login(request, business_owner)

				# redirect to home or dashboard after successful sign in
				return redirect('/dashboard/')
		
		else: # passwords don't match
			return render(request, "index.html", context={"auth_error": "passwords don't match"})
	
	else: # if the request came from somewhere else, ie. request is not valid
		return redirect('/')


@csrf_protect
def signin_view(request):
	# make sure the request came from the sign in form
	if request.method == "POST" and "signin-btn" in request.POST:
		username = request.POST['username']
		password = request.POST['psw']
		business_owner = authenticate(request, username=username, password=password)
		
		if business_owner is not None: # user exists, valid username & password
			login(request, business_owner)
			# redirect to home or dashboard after successful sign in
			return redirect('/dashboard/')

		else: # invalid username/password
			return render(request, "index.html", context={"auth_error": "login fail"})
	else: # if the request came from somewhere else, ie. request is not valid
		return redirect('/')

@login_required
@csrf_protect
def signout_view(request):
	logout(request)
	return redirect('/')


@login_required
@csrf_protect
def dashboard_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	prompt = "none"

	if request.method == "POST" and "import-data" in request.POST:
		if 'inventory-table' in request.FILES:
			prompt = import_inventory_table(request, business_owner)
					
		if 'products-table' in request.FILES:
			prompt = import_products_table(request, business_owner)

		if 'sales-table' in request.FILES:
			prompt = import_sales_table(request, business_owner)

	return render(request, "dashboard.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "dashboard", "prompt": prompt})


def import_inventory_table(request, business_owner):
	inventory_file = request.FILES['inventory-table']
	if not inventory_file.name.endswith('.csv'):
		prompt = "unsuccessful-ingredient-import-prompt"
		return prompt
	inventory_lines = inventory_file.read().decode("utf-8")
	lines = inventory_lines.split("\n")
	for line in lines[1:]:
		if line == '':
			pass
		else:
			columns = line.split(",")
			try:
				temporary = IngredientRecord.objects.get(ingredient_name=columns[0], owner=business_owner)
				temporary.cost = columns[1]
				temporary.units = columns[2]
				temporary.daily_units = columns[3]
				temporary.save()
			except ObjectDoesNotExist:
				temporary = IngredientRecord(
					ingredient_name=columns[0], cost=columns[1],units=columns[2], daily_units=columns[3], owner=business_owner)
				temporary.save()
	prompt = "successful-ingredient-import-prompt"
	return prompt


def import_products_table(request, business_owner):
	products_file = request.FILES['products-table']
	if not products_file.name.endswith('.csv'):
		prompt = "unsuccessful-product-import-prompt"
		return prompt
	products_lines = products_file.read().decode("utf-8")
	products_data = products_lines.split("\n")
	products_data[0] = products_data[0].split(",")
	products_data[0][-1] = products_data[0][-1].replace("\r","")
	last_ingr_index = len(products_data[0])
	first_ingr_index = products_data[0].index("price")+1
	for i in range(1,len(products_data)-1):
		products_data[i] = products_data[i].split(",")
		products_data[i][1] = float(products_data[i][1]);  # price
		products_data[i][first_ingr_index:] = [int(x) for x in products_data[i][first_ingr_index:]] # convert ingredients quantity to integer
		ingr = {}
		for j in range(first_ingr_index,last_ingr_index):
			quantity = products_data[i][j]
			if quantity != 0:
				ingr[products_data[0][j]] = quantity
		try:
			temp_product = ProductRecord.objects.get(product_name=products_data[i][0],owner=business_owner)
			temp_product.price = products_data[i][1]
			temp_product.ingredients = ingr
			temp_product.update_cost()
			temp_product.save()
		except ObjectDoesNotExist:
			temp_product = ProductRecord(
				product_name=products_data[i][0],price=products_data[i][1],ingredients=ingr,owner=business_owner)
			temp_product.save()
			temp_product.update_cost()
	prompt = "successful-product-import-prompt"
	return prompt

def import_sales_table(request, business_owner):
	sales_file = request.FILES['sales-table']
	if not sales_file.name.endswith('.csv'):
		prompt = "unsuccessful-sales-import-prompt"
		return prompt
	sales_lines = sales_file.read().decode("utf-8")
	sales_data = sales_lines.split("\n")
	sales_data[0] = sales_data[0].split(",")
	sales_data[0][1] = sales_data[0][1].replace('\r','')
	for i in range(1,len(sales_data)-1):
		sales_data[i] = sales_data[i].split(",")
		sales_data[i][0] = datetime.strptime(sales_data[i][0],"%Y-%m-%d").date()
		sales_data[i][1] = sales_data[i][1].split("|")
		sales = {}
		for j in range(len(sales_data[i][1])):
			sales_data[i][1][j] = sales_data[i][1][j].split("/")
			sales_data[i][1][j][-1] = int(sales_data[i][1][j][-1])
			prod_name = sales_data[i][1][j][0]
			num_sales = sales_data[i][1][j][1]
			sales[prod_name] = num_sales
		try:
			temp_sales = SalesRecord.objects.get(date=sales_data[i][0],sales_report=sales,owner=business_owner)
			temp_sales.date = sales_data[i][0]
			temp_sales.salesOfEachProduct = sales
			temp_sales.save()
		except ObjectDoesNotExist:
			temp_sales = SalesRecord(date=sales_data[i][0],sales_report=sales,owner=business_owner)
			temp_sales.save()
	prompt = "successful-sales-import-prompt"
	return prompt


@login_required
@csrf_protect
def profile_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	prompt = "none"

	if request.method == "POST" and "save-btn" in request.POST:
		new_full_name = request.POST["new-full-name"]
		new_business_name = request.POST["new-business-name"]
		business_owner.full_name = new_full_name
		business_owner.business_name = new_business_name
		business_owner.save()
		prompt = "saved-profile-changes"


	return render(request, "profile.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "profile", "prompt": prompt})




@login_required
@csrf_protect
def products_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	products_data = ProductRecord.objects.filter(owner=business_owner).order_by("id")
	inventory_data = IngredientRecord.objects.filter(owner=business_owner).order_by("id")
	update_all_products()
	prompt = "none"

	if request.method == "POST":
		if "add-product-btn" in request.POST:
			prompt = add_product_record(request, business_owner)
		elif "edit-product-btn" in request.POST:
			prompt = edit_product_record(request, business_owner)
		elif "delete-product-btn" in request.POST:
			prompt = delete_product_record(request, business_owner)


	return render(request, "products.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name, "full_name": business_owner.full_name, 
		"page": "products", "products_data": products_data, "inventory_data": inventory_data, "prompt": prompt})


def add_product_record(request, business_owner):
	prompt = "none"
	try:
		new_product_name = request.POST['new-product-name']
		new_product_price = request.POST['new-product-price']
		new_product_ingredients = {}
		for key in request.POST:
			if "name-input-row" in key:
				name_qty_input_row_id = key.replace("name-input-row-", "")
				name = request.POST[key]
				qty = request.POST["qty-input-row-" + name_qty_input_row_id]
				new_product_ingredients[name] = int(qty)
		temporary = ProductRecord(
			product_name=new_product_name, price=new_product_price, ingredients=new_product_ingredients, owner=business_owner)

		temporary.update_cost()
		temporary.save()
		prompt = "successful-product-add-prompt"
	except Exception as e:
		print(e)
		prompt = "invalid-product-ingredients-input"

	return prompt


def edit_product_record(request, business_owner):
	prompt = "none"
	try:
		edit_id = request.POST['edit-product-record-id']
		edit_product_name = request.POST['edit-product-name']
		edit_product_price = request.POST['edit-product-price']

		edit_product_ingredients = {}
		for key in request.POST:
			if "name-input-row" in key:
				name_qty_input_row_id = key.replace("name-input-row-", "")
				name = request.POST[key]
				qty = request.POST["qty-input-row-" + name_qty_input_row_id]
				edit_product_ingredients[name] = int(qty)

		record = ProductRecord.objects.get(id=edit_id)
		record.product_name = edit_product_name
		record.price = edit_product_price
		record.ingredients = edit_product_ingredients
		record.save()
		record.update_cost()
		prompt = "successful-product-edit-prompt"
	except:
		prompt = "invalid-product-ingredients-input"
	
	return prompt

def delete_product_record(request, business_owner):
	prompt = "none"
	delete_id = request.POST['delete-product-record-id']
	delete_record = ProductRecord.objects.get(id=delete_id)
	delete_record.delete()
	prompt = "successful-product-delete-prompt"

	return prompt




@login_required
@csrf_protect
def inventory_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	inventory_data = IngredientRecord.objects.filter(owner=business_owner).order_by("id")
	prompt = "none"
	if request.method == "POST":
		if "add-ingredient-btn" in request.POST:
			prompt = add_ingredient_record(request, business_owner)
		elif "edit-ingredient-btn" in request.POST:
			prompt = edit_ingredient_record(request, business_owner)
		elif "delete-ingredient-btn" in request.POST:
			prompt = delete_ingredient_record(request, business_owner)

	return render(request, "inventory.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "inventory", "inventory_data": inventory_data, "prompt": prompt})


def add_ingredient_record(request, business_owner):
	prompt = "none"
	new_ingredient_name = request.POST['new-ingredient-name']
	new_ingredient_cost = request.POST['new-ingredient-cost']
	new_total_units = request.POST['new-total-units']
	new_daily_units = request.POST['new-daily-units']
	temporary = IngredientRecord(
		ingredient_name=new_ingredient_name, cost=new_ingredient_cost, units=new_total_units, daily_units=new_daily_units, owner=business_owner)
	temporary.save()
	prompt = "successful-ingredient-add-prompt"
	
	update_all_products()
	return prompt


def edit_ingredient_record(request, business_owner):
	prompt = "none"

	edit_id = request.POST['edit-ingredient-record-id']
	edit_ingredient_name = request.POST['edit-ingredient-name']
	edit_ingredient_cost = request.POST['edit-ingredient-cost']
	edit_total_units = request.POST['edit-ingredient-total-units']
	edit_daily_units = request.POST['edit-ingredient-daily-units']
	record = IngredientRecord.objects.get(id=edit_id)
	record.ingredient_name = edit_ingredient_name
	record.cost = edit_ingredient_cost
	record.units = edit_total_units
	record.daily_units = edit_daily_units
	record.save()
	prompt = "successful-ingredient-edit-prompt"

	update_all_products()

	return prompt


def delete_ingredient_record(request, business_owner):
	prompt = "none"

	delete_id = request.POST['delete-ingredient-record-id']
	delete_record = IngredientRecord.objects.get(id=delete_id)
	delete_record.delete()
	prompt = "successful-ingredient-delete-prompt"

	update_all_products()
	return prompt


@login_required
@csrf_protect
def sales_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	products_data = ProductRecord.objects.filter(owner=business_owner).order_by("id")
	sales_data = SalesRecord.objects.filter(owner=business_owner).order_by("id")
	prompt = "prompt"


	return render(request, "sales.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "sales", "sales_data": sales_data, "products_data": products_data,
		"prompt": prompt})




def add_sales_record(request, business_owner):
	prompt = "none"

	return prompt



def edit_sales_record(request, business_owner):
	prompt = "none"

	return prompt


def delete_sales_record(request, business_owner):
	prompt = "none"

	return prompt



@login_required
@csrf_protect
def production_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	products_data = ProductRecord.objects.filter(owner=business_owner).order_by("id")


	return render(request, "production.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "production"})



def add_production_record(request, business_owner):
	prompt = "none"

	return prompt


def edit_production_record_view(request, business_owner):
	prompt = "none"

	return prompt



def delete_production_record_view(request, business_owner):
	prompt = "none"

	return prompt




@login_required
def profit_tracker_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)

	return render(request, "profit_tracker.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "profit-tracker"})










