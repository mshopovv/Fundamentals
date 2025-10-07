def people_in_wagons():
    number_of_wagons = [0] * int(input())

    while True:
        command = input().split()

        if command[0] == "End":
            print(number_of_wagons)
            break

        elif command[0] == "add":
            number_of_wagons[-1] += int(command[1])

        elif command[0] == "insert":
            current_index = int(command[1])
            number_of_wagons[current_index] += int(command[2])

        elif command[0] == "leave":
            current_index = int(command[1])
            number_of_wagons[current_index] -= int(command[2])

people_in_wagons()