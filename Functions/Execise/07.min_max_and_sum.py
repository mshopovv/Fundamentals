def min_max_and_sum(all_numbers: list) -> str:
    min_number = min(all_numbers)
    max_number = max(all_numbers)
    sum_of_numbers = sum(all_numbers)
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_of_numbers}"

numbers_input = input().split()
numbers_as_integers = []
for number in numbers_input:
    numbers_as_integers.append(int(number))

print(min_max_and_sum(numbers_as_integers))