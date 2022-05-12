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


def get_avg_daily_profit(BusinessOwner):
    sales_data = SalesRecord.objects.filter(owner=BusinessOwner)
    avg_profit = 0
    if len(sales_data) > 0:
        for sales in sales_data:
            avg_profit += sales.profit
        avg_profit = avg_profit / len(sales_data)

    return avg_profit


def get_avg_daily_expenses(BusinessOwner):
    production_data = ProductionRecord.objects.filter(owner=BusinessOwner)
    avg_expenses = 0
    if len(production_data) > 0:
        for production in production_data:
            avg_expenses += production.expenses
        avg_expenses = avg_expenses / len(production_data)
    return avg_expenses

def get_objective_eqn(Products_data,avg_sales_product):
    coeffs = []
    for prod in avg_sales_product:
        curr_product = Products_data.get(product_name = prod)
        coefficient = (avg_sales_product[prod]*float(curr_product.price)) - float(curr_product.cost)
        coeffs.append(coefficient)
    return coeffs

def convert_to_profit(n,avg_sales_product,products_data):
    sX = [avg_sales_product[key] for key in avg_sales_product]
    profit = round(-n.fun)
    for i in range(len(n.x)):
        profit -= sX[i]*float(products_data[i].price)*(n.x[i]- 1)
    return round(profit)

def update_available_units(business_owner,production_report,products_data,ingredients_data,choice = "add"):
    for prod in production_report:
        prod_record = None
        try:
            prod_record = products_data.get(product_name=prod)
            for ingr in prod_record.ingredients:
                ingr_record = None
                try:
                    ingr_record = ingredients_data.get(ingredient_name=ingr)
                    update_value = production_report[prod]*prod_record.ingredients[ingr]
                    update_value = (-1)*update_value if choice == "add" else update_value
                    ingr_record.units = ingr_record.units + update_value
                    ingr_record.daily_units = ingr_record.daily_units + update_value
                    ingr_record.save()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

def update_available_units_edit(business_owner,old_production_report,new_production_report,products_data,ingredients_data):
    update_available_units(business_owner,old_production_report,products_data,ingredients_data,"delete")
    update_available_units(business_owner,new_production_report,products_data,ingredients_data,"add")