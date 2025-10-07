words = input().split()
palindrome_word = input()

palindrome_words = [word for word in words if word == word[::-1]]
counter = palindrome_words.count(palindrome_word)

print(palindrome_words)
print(f'Found palindrome {counter} times')