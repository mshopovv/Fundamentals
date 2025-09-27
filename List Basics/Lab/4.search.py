number_of_lines = int(input())
keyword = input()

list_of_strings = []

for _ in range(number_of_lines):
    new_string = input()
    list_of_strings.append(new_string)

print(list_of_strings)

filtered_strings =[]

for _string in list_of_strings:
    if keyword in _string:
        filtered_strings.append(_string)

print(filtered_strings)
