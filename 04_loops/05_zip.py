names = ["Shani", "Meera", "Sam", "Ali"]


bills = [50, 70, 100, 55]

for name, bill in zip(names, bills):
    print(f"{name}- {bill}$")