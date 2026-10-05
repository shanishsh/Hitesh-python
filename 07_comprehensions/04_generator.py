daily_sales = [5, 10, 12, 7, 3, 50, 100]

total_cups = sum(sale for sale in daily_sales if sale>5)

print(total_cups)