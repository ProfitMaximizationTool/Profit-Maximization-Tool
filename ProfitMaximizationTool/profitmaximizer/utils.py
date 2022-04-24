from profitmaximizer.models import BusinessOwner, IngredientRecord, ProductRecord, SalesRecord, ProductionRecord

def update_all_products(BusinessOwner):
    for prod in ProductRecord.objects.filter(owner=BusinessOwner):
        prod.update_cost()

def update_all_revenues(BusinessOwner):
    for sales in SalesRecord.objects.filter(owner=BusinessOwner):
        sales.update_revenue()

def update_all_profit(BusinessOwner):
    for sales in SalesRecord.objects.filter(owner=BusinessOwner):
        sales.update_profit()

def update_all_expenses(BusinessOwner):
    for prod in ProductionRecord.objects.filter(owner=BusinessOwner):
        prod.update_expenses()

def get_avg_sales(BusinessOwner):
    avg_sales_prod = {}
    for prod in ProductRecord.objects.filter(owner=BusinessOwner):
        avg_sales_prod[prod.product_name] = 0
    for sales in SalesRecord.objects.filter(owner=BusinessOwner):
        for product in sales.sales_report:
            if product in avg_sales_prod:
                avg_sales_prod[product] += sales.sales_report[product]
    for prod in avg_sales_prod:
        avg_sales_prod[prod] /= len(SalesRecord.objects.filter(owner=BusinessOwner))
    return avg_sales_prod

def get_objective_eqn(Products_data,avg_sales_product):
    coeffs = []
    for prod in avg_sales_product:
        curr_product = Products_data.get(product_name = prod)
        coefficient = (avg_sales_product[prod]*float(curr_product.price)) - float(curr_product.cost)
        coeffs.append(coefficient)
    return coeffs

