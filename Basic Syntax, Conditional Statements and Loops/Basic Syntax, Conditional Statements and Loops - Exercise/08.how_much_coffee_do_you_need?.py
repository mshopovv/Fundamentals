coffees = 0

while True:
    command = input()
    if command == "END":
        break
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)