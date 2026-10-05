users = [
    {"id": 1, "total": 100, "coupon": "p20"},
    {"id": 2, "total": 200, "coupon": "p30"},
    {"id": 3, "total": 300, "coupon": "p40"}
]

discounts = {
    "p20":(0.2, 0),
    "p30":(0.3, 0),
    "p40":(0.5, 10)
}

for user in users:
    if user["coupon"] in discounts: 
        user["total"]=user["total"]-user["total"]*discounts[user["coupon"]][0]
        

for user in users:
    print(f"total- {user['total']}")