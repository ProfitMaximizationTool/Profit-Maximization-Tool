from django.contrib import admin

# Register your models here.

from .models import BusinessOwner
from .models import IngredientRecord

admin.site.register(BusinessOwner)
admin.site.register(IngredientRecord)