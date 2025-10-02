def odd_even_sum(numbers: str) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in numbers:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

single_number = input()
print(odd_even_sum(single_number))