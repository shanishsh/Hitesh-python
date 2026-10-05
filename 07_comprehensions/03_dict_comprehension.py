tea_prices_inr ={
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd={key:value/100 for key,value in tea_prices_inr.items() }

print(tea_prices_usd)