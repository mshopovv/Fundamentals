beggars_income = input().split(", ")
beggars_income_int = []

for income in beggars_income:
    beggars_income_int.append(int(income))

number_of_beggars = int(input())

beggars_sums = []

start_index = 0

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(beggars_income_int), number_of_beggars):
        current_beggar_sum += beggars_income_int[index]
    beggars_sums.append(current_beggar_sum)
    start_index += 1

print(beggars_sums)