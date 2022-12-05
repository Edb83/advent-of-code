import env
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

elves = sorted([sum([int(cal) for cal in elf.splitlines()]) for elf in puzzle.input_data.split('\n\n')], reverse=True)

print(max(elves))
print(sum(elves[:3]))
