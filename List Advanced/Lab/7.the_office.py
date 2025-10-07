from functools import reduce

def happiness_evaluator(employees_happiness: list, factor: int) -> str:
    improved_happiness = list(map(lambda x: x * factor, employees_happiness))
    average_happiness = (reduce(lambda x, y: x + y, employees_happiness) * factor) / len(employees_happiness)
    happy_count = sum(number >= average_happiness for number in improved_happiness)
    total_count = len(employees_happiness)
    message = 'happy' if happy_count >= total_count / 2 else 'not happy'
    return f'Score: {happy_count}/{total_count}. Employees are {message}!'

happiness = list(map(int, input().split()))
improvement_factor = int(input())
evaluation = happiness_evaluator(happiness, improvement_factor)
print(evaluation)