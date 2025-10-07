to_do_notes = [0] * 10

while True:
    command = input().split('-')
    if command[0] == "End":
        break
    priority_index = int(command[0]) - 1
    note = command[1]
    to_do_notes.pop(priority_index)
    to_do_notes.insert(priority_index, note)

result = [note for note in to_do_notes if note != 0]
print(result)
