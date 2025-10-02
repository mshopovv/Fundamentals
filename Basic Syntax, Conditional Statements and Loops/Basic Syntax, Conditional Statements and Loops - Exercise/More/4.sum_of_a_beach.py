text = input()

text_lower = text.lower()
words = ["sand", "water", "fish", "sun"]

total_count = sum(text_lower.count(word) for word in words)

print(total_count)