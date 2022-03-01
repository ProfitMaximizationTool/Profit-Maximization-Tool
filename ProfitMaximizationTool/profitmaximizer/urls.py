from django.urls import path

from . import views

urlpatterns = [
	path('', views.index_view, name='index'),
	path('home/', views.home_view, name='home'),
]