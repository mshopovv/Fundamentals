level_of_fire = input().split("#")
amount_of_water = int(input())

effort = 0
total_fire = 0

print("Cells:", end = "\n")
for current_fire in level_of_fire:
    cell = current_fire.split(" = ")
    type_of_fire = cell[0]
    cell_value = int(cell[1])
    if ((type_of_fire == "High" and 81 <= cell_value <= 125) or
        (type_of_fire == "Medium" and 51 <= cell_value <= 80) or
        (type_of_fire == "Low" and 1 <= cell_value <= 50)):
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            print(f" - {cell_value}", end = "\n")
        else:
            continue
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")
