from math import factorial

def factorials(num1: int, num2: int) -> int:
    factorial1 = factorial(num1)
    factorial2 = factorial(num2)
    return factorial1 / factorial2

first_number = int(input())
second_number = int(input())
division_of_factorials = factorials(first_number, second_number)

print(f"{division_of_factorials:.2f}")