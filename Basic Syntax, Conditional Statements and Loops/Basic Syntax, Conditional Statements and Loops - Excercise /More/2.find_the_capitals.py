string = input()

upper_cases = []

for i, character in enumerate(string):
    if 65 <= ord(character) <= 90:
        upper_cases += [i]

print(upper_cases)