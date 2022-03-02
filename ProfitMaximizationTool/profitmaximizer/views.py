from distutils import core
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from profitmaximizer.models import BusinessOwner
from django.core.exceptions import ObjectDoesNotExist

def index_view(request):
	if request.method == "POST":
		# sign up
		if "signup-btn" in request.POST:
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
			
			else: # passwords don't match
				return render(request, "index.html", context={"auth_error": "passwords don't match"})

		# sign in
		if "signin-btn" in request.POST:
			username = request.POST['username']
			password = request.POST['psw']
			business_owner = authenticate(request, username=username, password=password)
			
			if business_owner is not None: # user exists, valid username & password
				login(request, business_owner)
			else: # invalid username/password
				return render(request, "index.html", context={"auth_error": "login fail"})

		# redirect to home or dashboard after successful sign in or sign up
		return redirect('/home/')

	# default loading of index page
	return render(request, "index.html",  context={"auth_error": "none"})


@login_required
def home_view(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)

	# log out
	if request.method == "POST":
		if "logout-btn" in request.POST:
			logout(request)
			return redirect('/')
			
	return render(request, "home.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name,
		"full_name": business_owner.full_name})




