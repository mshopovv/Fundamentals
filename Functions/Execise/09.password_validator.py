def check_length(some_password):
    if 6 <= len(some_password) <= 10:
        return True
    return "Password must be between 6 and 10 characters"

def check_characters(some_password):
    if some_password.isalnum():
        return True
    return "Password must consist only of letters and digits"

def check_number_of_digits(some_password):
    digits_count = 0
    for symbol in some_password:
        if symbol.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    return "Password must have at least 2 digits"

def validate_password(some_password: str) -> list:
    is_valid = []
    is_valid.append(check_length(some_password))
    is_valid.append(check_characters(some_password))
    is_valid.append(check_number_of_digits(some_password))
    for index in range(len(is_valid) - 1, -1, -1):
        if isinstance(is_valid[index], bool):
            is_valid.pop(index)
    return is_valid

password = input()
password_is_not_valid = validate_password(password)
if password_is_not_valid:
    print("\n".join(password_is_not_valid))
else:
    print("Password is valid")
