energy = 100
coins = 100

day_completed = True

events = input().split("|")
for event in events:
    current_event = event.split("-")
    event_type = current_event[0]
    event_value = int(current_event[1])
    if event_type == "rest":
        initial_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        energy_spent = 30
        if energy >= energy_spent:
            coins += event_value
            energy -= energy_spent
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            day_completed = False
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")