key = int(input())
lines = int(input())
decrypted_word = ""

for line in range(lines):
    letter = input()
    letter_number = ord(letter) + key
    decrypted_word += chr(letter_number)

print(decrypted_word)
