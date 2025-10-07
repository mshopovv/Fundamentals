list_of_names = input().split(', ')
alphabetically_sorted = sorted(list_of_names)
sorter_by_length = sorted(alphabetically_sorted, key=len, reverse=True)

print(sorter_by_length)