number = int(input())

counts = [0] * 10

while number > 0:
    digit = number % 10
    counts[digit] += 1
    number //= 10

largest_number = 0
for digit in range(9, -1, -1):
    for _ in range(counts[digit]):
        largest_number = largest_number * 10 + digit

print(largest_number)

