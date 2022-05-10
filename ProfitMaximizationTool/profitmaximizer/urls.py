from django.conf import settings
from django.conf.urls.static import static
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

	path('dashboard/profit-optimizer/', views.profit_optimizer_view, name='profit-optimizer'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)