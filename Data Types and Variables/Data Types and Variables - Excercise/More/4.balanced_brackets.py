number_of_lines = int(input())

opening_bracket = 0
closing_bracket = 0
is_balanced = True

for line in range(number_of_lines):
    data = input()
    if data == "(":
        opening_bracket += 1
        if opening_bracket > 1:
            is_balanced = False
            break
    elif data == ")":
        closing_bracket += 1
        if opening_bracket == 0:
            is_balanced = False
            break
        opening_bracket = 0
        closing_bracket = 0

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")