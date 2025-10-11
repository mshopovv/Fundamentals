def electron_distribution(electrons: int) -> list:
    shells = []
    current_shell = 0
    while electrons > 0:
        current_shell += 1
        electrons_in_current_shell = 2 * (current_shell ** 2)
        if electrons < electrons_in_current_shell:
            shells.append(electrons)
        else:
            shells.append(electrons_in_current_shell)
        electrons -= electrons_in_current_shell
    return shells

number_of_electrons = int(input())
print(electron_distribution(number_of_electrons))
