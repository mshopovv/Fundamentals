def palindrome_check(numbers_as_strings: str) -> bool:
    return numbers_as_strings == numbers_as_strings[::-1]

positive_integers = input().split(", ")
for number in positive_integers:
    print(palindrome_check(number))
