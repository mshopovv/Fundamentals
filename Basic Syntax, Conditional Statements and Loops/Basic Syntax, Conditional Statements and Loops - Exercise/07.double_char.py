while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue

    for letter in string:
        print(letter * 2, end='')
    print()