def removed_vowels(string_text: str) -> str:
    adjusted_text = list(ch for ch in string_text if ch.lower() not in ['a', 'o', 'e', 'u', 'i'])
    return "".join(adjusted_text)

text_input = input()
print(removed_vowels(text_input))