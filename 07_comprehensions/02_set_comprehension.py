favourite_chais = [
    "Masala Chai","Green Tea","Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai"
]

# unique_chai = {chai for chai in favourite_chais if len(chai)}

# print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardmom","clove"],
    "Elaichi Chai": ["cardmom", "milk"],
    "Spicy Chai": ["ginger", "black pepper","clove"],
}

unique_spice = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spice)