# https://adventofcode.com/2023/day/6
import os
import re


def read_input(filename: str):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        with open(os.path.join(os.path.dirname(__file__), filename)) as file:
            raw_lines = file.readlines()

        if len(raw_lines) == 0:
            return ()

        new_string1 = re.sub(r'[^0-9\s]+', '', raw_lines[0].rstrip())
        new_string1 = re.sub(r'\s+', ' ', new_string1)

        new_string2 = re.sub(r'[^0-9\s]+', '', raw_lines[1].rstrip())
        new_string2 = re.sub(r'\s+', ' ', new_string2)

        times = [int(x) for x in new_string1.strip().split(' ')]
        dst = [int(x) for x in new_string2.strip().split(' ')]

    return times, dst


def solution_part1(filename: str) -> int:
    times, dst = read_input(filename)
    result = 1

    for i in range(len(dst)):
        t = times[i]
        d = dst[i]
        count = 0
        for x in range(1, t + 1):
            if x * (t - x) > d:
                count += 1
        result = result * count

    return result


def solution_part2(filename: str) -> int:
    times, dst = read_input(filename)
    result = 0

    t = int(''.join([str(x) for x in times]))
    d = int(''.join([str(x) for x in dst]))
    for x in range(1, t + 1):
        if x * (t - x) > d:
            result += 1

    return result


assert (solution_part1('data/input.test.txt') == 288)
print('Result Part 1: ', solution_part1('data/input.txt'))

assert (solution_part2('data/input.test.txt') == 71503)
print('Result Part 2: ', solution_part2('data/input.txt'))
