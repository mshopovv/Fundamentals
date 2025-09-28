list_of_strings = input().split( )
list_of_integers = []
for string in list_of_strings:
    list_of_integers.append(int(string))

numbers_to_be_removed = int(input())

for _ in range(numbers_to_be_removed):
    list_of_integers.remove(min(list_of_integers))

new_list_of_strings = []
for integer in list_of_integers:
    new_list_of_strings.append(str(integer))

print(", ".join(new_list_of_strings))