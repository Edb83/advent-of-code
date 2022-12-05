import env
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=4)
data = [line.split(',') for line in puzzle.input_data.splitlines()]
pairs = [[[int(num) for num in elf.split('-')] for elf in line] for line in data]

def fully_contains(pair):
    for elf in pair:
        other = pair[0] if pair[0] != elf else pair[1]
        if min(elf) <= min(other) and max(elf) >= max(other): return True

def part_one():
    fully_contains_total = 0
    for pair in pairs:
        if fully_contains(pair):
            fully_contains_total += 1

    return fully_contains_total

def has_no_overlap(pair):
    return min(pair[0]) > max(pair[1]) or max(pair[0]) < min(pair[1])

def part_two():
    has_overlap_total = len(pairs)
    for pair in pairs:
        if has_no_overlap(pair):
            has_overlap_total -= 1
    return has_overlap_total

print(part_one())
print(part_two())
