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

def get_avg_sales():
    avg_sales_prod = {}
    for prod in ProductRecord.objects.all():
        avg_sales_prod[prod.product_name] = 0
    for sales in SalesRecord.objects.all():
        for product in sales.sales_report:
            if product in avg_sales_prod:
                avg_sales_prod[product] += sales.sales_report[product]
    for prod in avg_sales_prod:
        avg_sales_prod[prod] /= len(SalesRecord.objects.all())
    return avg_sales_prod

def get_objective_eqn(avg_sales_product):
    coeffs = []
    for prod in avg_sales_product:
        curr_product = ProductRecord.objects.get(product_name = prod)
        coefficient = (avg_sales_product[prod]*float(curr_product.price)) - float(curr_product.cost)
        coeffs.append(coefficient)
    return coeffs

