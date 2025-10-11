text_input = input().split()

even_length_words = [text for text in text_input if len(text) % 2 == 0]

print('\n'.join(even_length_words))