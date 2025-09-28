gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    command_list = command.split()
    action_part = command_list[0]

    if action_part == "OutOfStock":
        gift_part = command_list[1]
        for index in range(len(gifts)):
            if gifts[index] == gift_part:
                gifts[index] = "None"

    elif action_part == "Required":
        gift_part = command_list[1]
        index_part = int(command_list[2])
        if 0 <= index_part < len(gifts):
            gifts[index_part] = gift_part

    elif action_part == "JustInCase":
        gift_part = command_list[1]
        if gifts:
            gifts[-1] = gift_part

adjusted_gifts = []
for gift in gifts:
    if gift != "None":
        adjusted_gifts.append(gift)

print(" ".join(adjusted_gifts))