numbers = list(map(int, input().split(', ')))

even_numbers_index = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(even_numbers_index)