def calculate_total_sales(sales_totals):
    total = 0.0
    for item in sales_totals.values():
        quantity = item.get("quantity", 0)
        price = item.get("price", 0)
        total += quantity * price
    return total

def calculate_average_sales(sales_totals):
    """Calculate the average sales per item."""
    if not sales_totals:
        return 0.0 

    total_sales = 0
    for item in sales_totals.values():
        total_sales += item["quantity"] * item["price"]
    
    return total_sales / len(sales_totals)

def filter_to_better_than_average_sales(sales_totals):
    if not sales_totals:
        return {}
    total_sales = sum(item["quantity"] * item["price"] for item in sales_totals.values())
    average_sales = total_sales / len(sales_totals)
    filtered_sales = {}
    for item, details in sales_totals.items():
        if details["quantity"] * details["price"] > average_sales:
            filtered_sales[item] = details
    return filtered_sales
    

def ninety_nine_bottles(count, beverage):
    pass