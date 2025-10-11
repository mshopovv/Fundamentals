repeat_strings = lambda strings, multiplier: strings * multiplier

text = input()
counter = int(input())
result = repeat_strings(text, counter)
print(result)
