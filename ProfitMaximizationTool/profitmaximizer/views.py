from decimal import Decimal
from distutils import core
from tkinter.tix import AUTO
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from profitmaximizer.models import BusinessOwner, IngredientRecord, ProductRecord
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect


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
def dashboard_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
			
	if request.method == "POST" and "import-data" in request.POST:
		if 'inventory-table' in request.FILES:
			inventory_file = request.FILES['inventory-table']
			if not inventory_file.name.endswith('.csv'):
				return render(request, "dashboard.html", 
				{"username": business_owner.username, "business_name": business_owner.business_name,
				"full_name": business_owner.full_name, "page": "dashboard"})
			inventory_lines = inventory_file.read().decode("utf-8")
			lines = inventory_lines.split("\n")
			for line in lines[1:]:
				if line == '':
					pass
				else:
					columns = line.split(",")
					temporary = IngredientRecord(id=columns[0],ingredient_name=columns[1], cost=columns[2],units=columns[3], daily_units=columns[4], owner_id=business_owner.user_ptr_id)
					temporary.save()
					
		if 'products-table' in request.FILES:
			products_file = request.FILES['products-table']
			if not products_file.name.endswith('.csv'):
				return render(request, "dashboard.html", 
				{"username": business_owner.username, "business_name": business_owner.business_name,
				"full_name": business_owner.full_name, "page": "dashboard"})
			products_lines = products_file.read().decode("utf-8")
			products_data = products_lines.split("\n")
			last_ingr_index = len(products_data[0])
			first_ingr_index = 4
			products_data[0] = products_data[0].split(",")
			products_data[0][-1] = products_data[0][-1].replace("\r","")
			for i in range(1,len(products_data)-1):
				products_data[i] = products_data[i].split(",")
				products_data[i][0] = int(products_data[i][0])
				products_data[i][2] = float(products_data[i][2]); products_data[i][3] = float(products_data[i][3])
				products_data[i][4:] = [int(x) for x in products_data[i][4:]]
				ingr = {products_data[0][j]: products_data[i][j] for j in range(4,len(products_data[i]))}
				temp_product = ProductRecord(id=products_data[i][0],productName=products_data[i][1],cost=products_data[i][2],price=products_data[i][3],ingredients=ingr,owner_id=business_owner.user_ptr_id)
				temp_product.save()

	return render(request, "dashboard.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "dashboard"})


@login_required
def products_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	frgn_key = business_owner.user_ptr_id
	products_data = ProductRecord.objects.filter(owner_id=frgn_key).order_by("id")
	return render(request, "products.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "products", "products_data": products_data})

@login_required
def inventory_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)
	frgn_key = business_owner.user_ptr_id
	inventory_data = IngredientRecord.objects.filter(owner_id=frgn_key).order_by("units")
	return render(request, "inventory.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "inventory", "inventory_data": inventory_data})

@login_required
def sales_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)

	return render(request, "sales.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "sales"})

@login_required
def production_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)

	return render(request, "production.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "production"})

@login_required
def profit_tracker_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)

	return render(request, "profit_tracker.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name, "page": "profit-tracker"})

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
def add_ingredient_view(request):
	# redirect to inventory page
	if request.method == "POST" and "add-ingredient-btn" in request.POST:
		print("-------------------")
		print(request.POST)
	pass


@login_required
@csrf_protect
def edit_ingredient_view(request):
	# redirect to inventory page
	if request.method == "POST" and "edit-ingredient-btn" in request.POST:
		print("-------------------")
		print(request.POST)
	pass


@login_required
@csrf_protect
def delete_ingredient_view(request):
	# redirect to inventory page
	if request.method == "POST" and "delete-ingredient-btn" in request.POST:
		print("-------------------")
		print(request.POST)
	pass
