from profitmaximizer.models import BusinessOwner, IngredientRecord, ProductRecord, SalesRecord, ProductionRecord

def update_all_products():
    for prod in ProductRecord.objects.all():
        prod.update_cost()

def update_all_revenues():
    for sales in SalesRecord.objects.all():
        sales.update_revenue()

def update_all_profit():
    for sales in SalesRecord.objects.all():
        sales.update_profit()

def update_all_expenses():
    for prod in ProductionRecord.objects.all():
        prod.update_expenses()
