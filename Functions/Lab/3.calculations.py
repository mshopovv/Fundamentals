def calculation_func(operation: str, num1: int, num2: int) -> int:
    result = 0
    if operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 // num2
    elif operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    return result

operator = input()
first_number = int(input())
second_number = int(input())
calculation = calculation_func(operator, first_number, second_number)
print(calculation)
