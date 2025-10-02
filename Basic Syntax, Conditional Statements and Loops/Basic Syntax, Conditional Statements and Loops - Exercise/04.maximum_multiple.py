divisor = int(input())
boundary = int(input())
number = 0

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        number = current_number
        break

print(number)