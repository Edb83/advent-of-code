import env
from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2022, day=5)
stack_data = puzzle.input_data.splitlines()[:8]
instructions_data = puzzle.input_data.splitlines()[10:]

def parse_stack_data():
    inverted_stack_data = [stack_data[i-1] for i in range(len(stack_data), 0, -1)]
    cleaned = []
    for row in inverted_stack_data:
        # get odd columns (where crate info lives)
        odd_cols = [item[1] for item in enumerate(row) if item[0] % 2 == 1]
        # remove alternating columns that contain nothing
        trimmed = [i[1] for i in enumerate(odd_cols) if i[0] % 2 == 0]
        cleaned.append(''.join(trimmed))
    # remove empty values and flip the array 90 degrees
    return [[col for col in list(col) if ' ' not in list(col)] for col in zip(*cleaned)]
    
def parse_instructions_data():
    return [[int(num) for num in re.findall('\d+', instruction)] for instruction in instructions_data]

def get_answer(part):
    stacks = parse_stack_data()
    instructions = parse_instructions_data()
    for instruction in instructions:
        num, start, end = instruction
        # slice num items from tail of start list and reverse/don't depending on part
        stacks[end-1] += reversed(stacks[start-1][-num:]) if part == 1 else stacks[start-1][-num:]
        del stacks[start-1][-num:]
    return ''.join(str(stack[-1]) for stack in stacks)

print(get_answer(1))
print(get_answer(2))
