daily_sales = [5,3,4,7,4,8,10,9]


unique_dishes = sum(sale for sale in daily_sales if sale > 5)

print(unique_dishes)