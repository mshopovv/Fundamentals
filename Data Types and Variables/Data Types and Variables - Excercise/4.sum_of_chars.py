number_of_lines = int(input())
sum_of_characters = 0

for line in range(number_of_lines):
    character = input()
    sum_of_characters += ord(character)

print(f"The sum equals: {sum_of_characters}")