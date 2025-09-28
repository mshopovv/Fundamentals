items_to_sell = input().split("|")
budget = float(input())

money_spent = 0
money_gathered = 0

for item in items_to_sell:
    new_item = item.split("->")
    item_type = new_item[0]
    item_price = float(new_item[1])
    if ((item_type == "Clothes" and item_price <= 50.00) or
            (item_type == "Shoes" and item_price <= 35.00) or
            (item_type == "Accessories" and item_price <= 20.50)) and \
            item_price <= budget:
        budget -= item_price
        money_spent += item_price
        sold_price = item_price * 1.4
        print(f"{sold_price:.2f}", end = " ")
        money_gathered += sold_price

print(f"\nProfit: {(money_gathered - money_spent):.2f}")
if money_gathered + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")