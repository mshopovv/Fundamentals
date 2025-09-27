animal = []

for _ in range(3):
    data_input = input()
    animal.append(data_input)

animal[0], animal[2] = animal[2], animal[0]

print(animal)