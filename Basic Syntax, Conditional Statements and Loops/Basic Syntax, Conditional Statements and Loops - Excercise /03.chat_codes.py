number_of_messages = int(input())

for n in range(0, number_of_messages):
    chat_code = int(input())
    message = ""
    if chat_code == 88:
        message = "Hello"
    elif chat_code == 86:
        message = "How are you?"
    elif chat_code < 88 and chat_code != 86:
        message = "GREAT!"
    elif chat_code > 86:
        message = "Bye."
    print(message)