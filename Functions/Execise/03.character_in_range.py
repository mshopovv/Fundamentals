def characters_in_range(first: str, second: str) -> list:
    collected_symbols = []
    for symbol in range(ord(first) + 1, ord(second)):
        collected_symbols.append(chr(symbol))
    return collected_symbols


first_character = input()
second_character = input()
symbols = characters_in_range(first_character, second_character)
print(" ".join(symbols))