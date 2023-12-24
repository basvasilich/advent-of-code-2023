# https://adventofcode.com/2023/day/14
import os


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = [[''] * len(raw_lines) for _ in range(len(raw_lines[0].rstrip()))]

        if len(raw_lines) == 0:
            return ()

        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            for index, char in enumerate(line):
                if char != '.':
                    result[index][row] = char
            row += 1

        return result


def tilt(row: list[str]) -> list[str]:
    point_r = 0
    point_w = 0
    while point_r < len(row):
        char = row[point_r]
        if char == '#' and point_r < len(row):
            point_w = point_r + 1
        elif char == 'O':
            row[point_r] = ''
            row[point_w] = 'O'
            point_w += 1
        point_r += 1
    return row


def solution_part1(filename: str) -> int:
    m = read_input(filename)
    m_with_lilt = []
    for row in m:
        m_with_lilt.append(tilt(row))
    sum = 0
    for row in m:
        for index, char in enumerate(row):
            if char == 'O':
                sum += len(row) - index

    return sum


assert (solution_part1('data/input.test.txt') == 136)
print('Result Part 1: ', solution_part1('data/input.txt'))
