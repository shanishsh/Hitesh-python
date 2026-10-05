def add_vat(price, vat_rate):

    return price * (100 + vat_rate)/100

orders = [100, 150, 200]


for order in orders:
    print(f"Added vat is {add_vat(order,30)}")