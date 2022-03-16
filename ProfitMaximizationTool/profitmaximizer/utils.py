from profitmaximizer.models import BusinessOwner, IngredientRecord, ProductRecord

def update_all_products():
    for prod in ProductRecord.objects.all():
        prod.update_cost()