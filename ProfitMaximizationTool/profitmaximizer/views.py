from distutils import core
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from profitmaximizer.models import BusinessOwner

from django.core.exceptions import ObjectDoesNotExist
def index(request):
	if request.method == "POST":
		# sign up
		if "signup-btn" in request.POST:
			if request.POST['psw'] == request.POST['confirmpsw']:
				username = request.POST['username']
				password = request.POST['psw']
				business_name = request.POST['businessname']

				try:
					business_owner = BusinessOwner.objects.get(username = username)
					return render(request, "index.html")

				except ObjectDoesNotExist:
					business_owner = BusinessOwner.objects.create_user(username=username, email=None, password=password)
					business_owner.business_name = business_name
					business_owner.save()
					login(request, business_owner)
				
			else:
				return render(request, "index.html")

		# sign in
		if "signin-btn" in request.POST:
			username = request.POST['username']
			password = request.POST['psw']
			business_owner = authenticate(request, username=username, password=password)
			if business_owner is not None:
				login(request, business_owner)
			else:
				return render(request, "index.html")

		return redirect('/home/')

	return render(request, "index.html")



# @login_required
def home(request):
	business_owner = BusinessOwner.objects.get(username=request.user.username)

	# log out
	if request.method == "POST":
		if "logout-btn" in request.POST:
			logout(request)
			return redirect('/')
			
	return render(request, "home.html", 
		{"username": business_owner.username, "business_name": business_owner.business_name})




