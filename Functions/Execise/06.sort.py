def ascending_order(ascending_list: list) -> list:
    return sorted(ascending_list)

numbers_input = input().split()
numbers_as_integers = []
for number in numbers_input:
    numbers_as_integers.append(int(number))

print(ascending_order(numbers_as_integers))