def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = some_number // 10
    not_loaded_percent = 10 - loaded_percent
    return f"{some_number}% [{'%' * loaded_percent}{'.' * not_loaded_percent}]\nStill loading..."

integer_input = int(input())
print(loading_bar(integer_input))