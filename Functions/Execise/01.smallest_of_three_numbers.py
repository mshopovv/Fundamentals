def find_smallest_number(numbers: list) -> int:
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = find_smallest_number([first_number, second_number, third_number])
print(smallest_number)

