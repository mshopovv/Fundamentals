number_of_lines = int(input())
numbers_list = []

for _ in range(number_of_lines):
    number = int(input())
    numbers_list.append(number)

command = input()

filtered_list = []

for _number in numbers_list:
    if command == "even" and _number % 2 == 0:
        filtered_list.append(_number)
    elif command == "odd" and _number % 2 != 0:
        filtered_list.append(_number)
    elif command == "negative" and _number < 0:
        filtered_list.append(_number)
    elif command == "positive" and _number >= 0:
        filtered_list.append(_number)

print(filtered_list)