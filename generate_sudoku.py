import random

def generate_sudoku():
    puzzle = []

    numbers = [0]* 9 + list(range(1,10))

    for _ in range(9):
        row = []
        for _ in range(9):
            rand_int = random.choice()
            row.append(rand_int)
        puzzle.append(row)

    return puzzle