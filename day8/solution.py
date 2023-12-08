# https://adventofcode.com/2023/day/8
import os
import re
import math


def read_input(filename: str) -> (str, dict[str, (str, str)], list[str]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        moves = ''
        tree = {}
        special_keys = []

        if len(raw_lines) == 0:
            return ()

        pointer = 0
        while pointer < len(raw_lines):
            line = raw_lines[pointer].rstrip()

            if pointer == 0:
                moves = line
                pointer += 2
            else:
                key, val_str = line.split(' = ')
                new_string = re.sub(r"[^1-9A-Z,]+", '', val_str.strip())
                val_l, val_r = new_string.split(',')
                tree[key] = (val_l, val_r)
                if key[2] == 'A':
                    special_keys.append(key)
                pointer += 1

        return moves, tree, special_keys


def get_next_move(moves: str, counter: int) -> 0 | 1:
    pointer = int(counter % len(moves))
    if moves[pointer] == 'L':
        return 0
    return 1


def check_current_keys(keys: list[str]) -> bool:
    counter = len(keys)
    for k in keys:
        if k[2] == 'Z':
            counter -= 1
    return counter == 0


def least_common_multiple(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // math.gcd(lcm, numbers[i])
    return lcm


def solution_part2(filename: str) -> int:
    moves, tree, special_keys = read_input(filename)
    result = []
    counter = 0
    while len(result) < len(special_keys):
        next_move = get_next_move(moves, counter)
        for i in range(len(special_keys)):
            special_keys[i] = tree[special_keys[i]][next_move]

            if special_keys[i][2] == 'Z':
                result.append(counter + 1)
        counter += 1
    return least_common_multiple(result)


def solution_part1(filename: str) -> int:
    moves, tree, _ = read_input(filename)
    counter = 0
    next_key = 'AAA'
    while next_key != 'ZZZ':
        next_move = get_next_move(moves, counter)
        next_key = tree[next_key][next_move]
        counter += 1
    return counter


assert (solution_part2('data/input3.test.txt') == 6)
assert (solution_part2('data/input.test.txt') == 2)
print('Result Part 2: ', solution_part2('data/input.txt'))

assert (solution_part1('data/input2.test.txt') == 6)
assert (solution_part1('data/input.test.txt') == 2)
print('Result Part 1: ', solution_part1('data/input.txt'))
