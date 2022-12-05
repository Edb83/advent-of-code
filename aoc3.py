import env
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=3)
rucksacks = puzzle.input_data.splitlines()

def get_priority(item):
    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return priorities.index(item) + 1

def part_one():
    total = 0
    for rucksack in rucksacks:
        length = len(rucksack)
        c1 = set(rucksack[:length//2])
        c2 = set(rucksack[length//2:])
        common_item = c1 & c2
        total += get_priority(common_item.pop())
    return total


def get_groups():
    """
    Split rucksacks at every nth iteration, converting contents to sets for later intersection
    """
    n = 3
    groups = [[set(sack) for sack in rucksacks[i:i+n]] for i in range(0, len(rucksacks), n)]
    return groups

def part_two():
    total = 0
    groups = get_groups()

    for group in groups:
        common_item = set.intersection(*group)
        total += get_priority(common_item.pop())
    return total

print(part_one())
print(part_two())
