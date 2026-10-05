menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)

num_list = [1,2,3,4,5,6,7,8,9,10,11]

even_list = [num for num in range(1,101) if num%2==0]

print(even_list)