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
	path('add-product-record/', views.add_product_record_view, name='add-product-record'),
	path('edit-product-record/', views.edit_product_record_view, name='edit-product-record'),
	path('delete-product-record/', views.delete_product_record_view, name='delete-product-record'),

	path('dashboard/inventory/', views.inventory_view, name='inventory'),
	path('add-ingredient-record/', views.add_ingredient_record_view, name='add-ingredient-record'),
	path('edit-ingredient-record/', views.edit_ingredient_record_view, name='edit-ingredient-record'),
	path('delete-ingredient-record/', views.delete_ingredient_record_view, name='delete-ingredient-record'),

	path('dashboard/sales/', views.sales_view, name='sales'),
	path('add-sales-record/', views.add_sales_record_view, name='add-sales-record'),
	path('edit-sales-record/', views.edit_sales_record_view, name='edit-sales-record'),
	path('delete-sales-record/', views.delete_sales_record_view, name='delete-sales-record'),

	path('dashboard/production/', views.production_view, name='production'),
	path('add-production-record/', views.add_production_record_view, name='add-production-record'),
	path('edit-production-record/', views.edit_production_record_view, name='edit-production-record'),
	path('delete-production-record/', views.delete_production_record_view, name='delete-production-record'),

	path('dashboard/profit-tracker/', views.profit_tracker_view, name='profit-tracker'),
]