current_version = list(map(int, input().split('.')))
current_version[-1] += 1

for index in range(len(current_version) - 1, 0, -1):
    if current_version[index] > 9:
        current_version[index] = 0
        current_version[index - 1] += 1


print('.'.join([str(index) for index in current_version]))