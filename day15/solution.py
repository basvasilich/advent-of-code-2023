# https://adventofcode.com/2023/day/15
import os


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        line = raw_lines[0].rstrip()
        result = []

        if len(raw_lines) == 0:
            return ()

        return line.split(',')


def hash_step(step: str) -> int:
    result = 0
    for character in step:
        result += ord(character)
        result *= 17
        result %= 256

    return result


def solution_part1(filename: str) -> int:
    steps = read_input(filename)
    result = 0
    for step in steps:
        result += hash_step(step)

    return result


assert (solution_part1('data/input.test.txt') == 52)
assert (solution_part1('data/input2.test.txt') == 1320)
print('Result Part 1: ', solution_part1('data/input.txt'))
