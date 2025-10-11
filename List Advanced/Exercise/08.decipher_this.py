secret_message = input().split()

deciphered_message = []

for word in secret_message:
    word = list(word)
    numbers_as_string = ""
    for index in range(len(word)):
        if word[index].isdigit():
            numbers_as_string += word[index]
        else:
            break
    numbers_as_letter = chr(int(numbers_as_string))
    word = [numbers_as_letter] + word[index:]

    word[1], word[-1] = word[-1], word[1]

    new_word = "".join(word)
    deciphered_message.append(new_word)

print(" ".join(deciphered_message))