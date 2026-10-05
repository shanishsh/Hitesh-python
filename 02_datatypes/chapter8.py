ingredients = ["water", "milk" ,"black tea"]

ingredients.append("sugar")
print(f"Ingridients are: {ingredients}")


ingredients.remove("water")
print(f"Ingridients are: {ingredients}")


spice_options = ["ginger", "cardamom"]

chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)

print(f"chai: {chai_ingredients}")