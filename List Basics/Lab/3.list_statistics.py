number_of_lines = int(input())
list_of_positives = []
list_of_negatives = []

for line in range(number_of_lines):
    number = int(input())
    if number >= 0:
        list_of_positives.append(number)
    else:
        list_of_negatives.append(number)

print(f"{list_of_positives}\n{list_of_negatives}")
print(f"Count of positives: {len(list_of_positives)}")
print(f"Sum of negatives: {sum(list_of_negatives)}")