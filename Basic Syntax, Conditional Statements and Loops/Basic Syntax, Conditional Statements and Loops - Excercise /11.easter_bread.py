budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_liter_milk = price_per_kg_flour * 1.25
price_per_loaf = price_per_kg_flour + price_per_pack_eggs + price_per_liter_milk / 4

number_of_loaves = 0
colored_eggs = 0
money_spent = 0

while budget - money_spent > price_per_loaf:
    number_of_loaves += 1
    money_spent += price_per_loaf
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

money_left = budget - money_spent
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")