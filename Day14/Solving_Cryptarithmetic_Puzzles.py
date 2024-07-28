def exhaustive_solve(puzzle, letters_to_assign):
    if not letters_to_assign:  # no more choices to make
        return puzzle_solved(puzzle)  # checks arithmetic to see if it works
    for digit in range(10):  # try all digits
        if assign_letter_to_digit(letters_to_assign[0], digit):
            if exhaustive_solve(puzzle, letters_to_assign[1:]):
                return True
            unassign_letter_from_digit(letters_to_assign[0], digit)
    return False  # nothing worked, need to backtrack
