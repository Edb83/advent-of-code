import env
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)

def chars_to_match(n):
    letters = puzzle.input_data
    current = []
    for i in range(n, len(letters) + n):
        current = letters[i-n:i]
        if len(set(current)) == len(current):
            return i

print(chars_to_match(4))
print(chars_to_match(14))
