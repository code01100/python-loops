
# for token in range (1,11):
#     print(f"Serving chai to token #{token}")



# for batch in range (1,5):
#     print (f"Preparing chai for batch #{batch}")


# orders = ["Alex", "Rick","Anna", "Laura","John"]

# for name in orders:
#     print(f"Order ready for {name}")


# menu = ["Green","Black", "Bergamot", "Lemon", "Ginger","Herbal"]

# for index, item in enumerate (menu, start=1):
#     print(f"{index} : {item} chai")


# names = ["Alex","Sam","Anna","Laura"]

# bills = [100,75,300,50]

# for name , amount in zip(names,bills):
#     print(f"{name} paid {amount} dollars")


# temperature = 40

# while temperature < 100:
#     print(f"Current temperature: {temperature}")
#     temperature +=15
# print (f"Water is ready")


# flavors = ["lemon", "mint","herbal","honey", "out of stock","discontinued"]

# for flavor in flavors:
#     if flavor =="out of stock":
#         continue
#     if flavor == "discontinued":
#         break
#     print(f"{flavor} item found")   
# print (f"Outside of loop") 


# staff = [("Alex",17), ("Brad",16),("Anna",12)]

# for name, age in staff:
#     if age <= 18:
#         print(f"{name} is eligible to manage the staff")
#         break
# else:
#     print(f"No one is eligible to manage the staff")


# using dictionary instead of repeated cases
users = [

    {"id": 1,"total": 100, "coupon": "P20"},
    {"id": 2,"total": 70, "coupon": "F40"},
    {"id": 3,"total": 90, "coupon": "S50"},
]

discounts ={
    "P20": (0.2,0),
    "F40": (0.5,0),
    "S50": (0,10)
}


for user in users:
    percent, fixed = discounts.get(user["coupon"], (0.0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of dollars {discount}")