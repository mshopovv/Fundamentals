def absolute_values(numbers_sequence: list) -> list:
    absolute_value_list = [abs(number) for number in numbers_sequence]
    return absolute_value_list

numbers_input = list(map(float, input().split()))
print(absolute_values(numbers_input))