from django.contrib import admin

# Register your models here.

from .models import BusinessOwner,IngredientRecord,ProductRecord, SalesRecord, ProductionRecord

admin.site.register(BusinessOwner)
admin.site.register(IngredientRecord)
admin.site.register(ProductRecord)
admin.site.register(SalesRecord)
admin.site.register(ProductionRecord)