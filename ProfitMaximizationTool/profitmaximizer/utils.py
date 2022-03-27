from profitmaximizer.models import BusinessOwner, IngredientRecord, ProductRecord, SalesRecord

def update_all_products():
    for prod in ProductRecord.objects.all():
        prod.update_cost()

def update_all_revenues():
    for sales in SalesRecord.objects.all():
        sales.update_revenue()