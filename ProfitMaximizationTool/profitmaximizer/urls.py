from django.urls import path

from . import views

urlpatterns = [
	path('', views.index_view, name='index'),
	path('signin/', views.signin_view, name='signin'),
	path('signup/', views.signup_view, name='signup'),
	path('signout/', views.signout_view, name='signout'),
	path('dashboard/', views.dashboard_view, name='dashboard'),
	path('dashboard/profile/', views.profile_view, name='profile'),
	path('dashboard/products/', views.products_view, name='products'),
	path('dashboard/inventory/', views.inventory_view, name='inventory'),
	path('dashboard/sales/', views.sales_view, name='sales'),
	path('dashboard/production/', views.production_view, name='production'),
	path('dashboard/profit-tracker/', views.profit_tracker_view, name='profit-tracker'),
	path('add-ingredient/', views.add_ingredient_view, name='add-ingredient'),
	path('edit-ingredient/', views.edit_ingredient_view, name='edit-ingredient'),
	path('delete-ingredient/', views.delete_ingredient_view, name='delete-ingredient'),
	path('add-product/', views.add_product_view, name='add-product'),
	path('edit-product/', views.edit_product_view, name='edit-product'),
	path('delete-product/', views.delete_product_view, name='delete-product'),
]