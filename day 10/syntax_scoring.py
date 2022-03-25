from enum import Enum
from typing import Optional

import numpy as np

from bracket_tree import Tree

input_path = './day 10/input.txt'

lines: list[str] = []

with open(input_path, 'r') as infile:
    for line in infile.readlines():
        if not line.isspace():
            lines.append(line.strip())

brackets_start: list[str] = ['(', '[', '{', '<']
brackets_end: list[str] = [')', ']', '}', '>']
brackets_score: list[int] = [3, 57, 1197, 25137]

brackets_match: dict[str, str] = {
    ')':'(', 
    ']':'[', 
    '}':'{', 
    '>':'<'
}

brackets_match_reverse = {v: k for k, v in brackets_match.items()}

def is_corrupted(line: str) -> tuple[bool, str]:
    brackets: list[str] = []

    for c in line:
        if c in brackets_start:
            brackets.append(c)
        elif c in brackets_end:
            if brackets_match[c] == brackets[-1]:
                brackets.pop()
            else:
                return True, c

    return False, ''

def part_one() -> int:
    score: int = 0

    for line in lines:
        is_corr, c = is_corrupted(line)
        if is_corr:
            score += brackets_score[brackets_end.index(c)]
        
    return score

print(f'--- PART ONE ---')
print(f'The sum of all the syntax errors is {part_one()}')

brackets_score_2: list[int] = [1, 2, 3, 4]

def complete_line(line: str) -> str:
    brackets: list[str] = []

    for c in line:
        if c in brackets_start:
            brackets.append(c)
        elif c in brackets_end:
            brackets.pop()

    output: str = ''.join(reversed([brackets_match_reverse[c] for c in brackets])) 
    return output

def calculate_score(s: str) -> int:
    score: int = 0

    for c in s:
        score *= 5
        score += brackets_score_2[brackets_end.index(c)]

    return score

def part_two() -> int:
    scores: list[int] = []

    for line in lines:
        is_corr, _ = is_corrupted(line)
        if is_corr:
            continue
        
        compl_s: str = complete_line(line)
        scores.append(calculate_score(compl_s))

    scores = sorted(scores)

    return scores[int((len(scores) - 1) / 2)]

print(f'--- PART TWO ---')
print(f'The median of the scores is {part_two()}')


