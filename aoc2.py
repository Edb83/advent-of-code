import env
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)
rounds = [round.replace(' ', '') for round in puzzle.input_data.splitlines()]

POINTS = {'A': 1, 'B': 2, 'C': 3}

OUTCOMES = {
    'AC': 0,
    'BA': 0,
    'CB': 0,
    'AA': 3,
    'BB': 3,
    'CC': 3,
    'AB': 6,
    'BC': 6,
    'CA': 6
}

def convert_choice(choice):
    return 'A' if choice == 'X' else 'B' if choice == 'Y' else 'C'

def convert_result(result):
    return 0 if result == 'X' else 3 if result == 'Y' else 6

def find_choice(string):
    result = convert_result(string[1])
    for k, v in OUTCOMES.items():
        if v == result and k[0] == string[0]:
            return k[1]

def get_answer(part):
    total_score = 0
    for round in rounds:
        them = round[0]
        you = convert_choice(round[1]) if part == 1 else find_choice(round)
        choice_score = POINTS[you]
        outcome_score = OUTCOMES[them + you]
        total_score += choice_score + outcome_score
    return total_score

print(get_answer(1))
print(get_answer(2))
