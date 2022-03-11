from django.contrib import admin

# Register your models here.

from .models import BusinessOwner
from .models import inventory_db

admin.site.register(BusinessOwner)
admin.site.register(inventory_db)