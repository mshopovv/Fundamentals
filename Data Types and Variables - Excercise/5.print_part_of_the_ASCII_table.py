start_index = int(input())
last_index = int(input())

for index in range(start_index, last_index + 1):
    if index == last_index:
        print(chr(index))
    else:
        print(chr(index), end = " ")