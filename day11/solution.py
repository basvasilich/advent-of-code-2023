# https://adventofcode.com/2023/day/11
import os
import itertools


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = []
        gals = []

        if len(raw_lines) == 0:
            return ()

        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            has_gals = False
            for col, char in enumerate(line):
                if char == '#':
                    has_gals = True
            if not has_gals:
                raw_lines.insert(row + 1, '.' * len(line))
                row += 2
            else:
                row += 1

        col = 0
        need_insert_cols = []
        while col < len(raw_lines[0].rstrip()):
            has_gals = False
            for row in range(len(raw_lines)):
                char = raw_lines[row][col]
                if char == '#':
                    has_gals = True
            if not has_gals:
                need_insert_cols.append(col)
            col += 1
        row = 0
        while row < len(raw_lines):
            line_arr = list(raw_lines[row].rstrip())
            for i, col_insert in enumerate(need_insert_cols):
                line_arr.insert(col_insert + 1 + i, '.')
            result.append(line_arr)
            row += 1

        for row in range(len(result)):
            for col in range(len(result[0])):
                char = result[row][col]
                if char == '#':
                    gals.append((row, col))
        return result, gals


def solution_part1(filename: str) -> int:
    result, gals = read_input(filename)
    pairs = list(itertools.combinations(gals, 2))
    sum = 0
    for g1, g2 in pairs:
        y1, x1 = g1
        y2, x2 = g2
        sum += abs(x1-x2) + abs(y2-y1)

    return sum


assert (solution_part1('data/input.test.txt') == 374)
print('Result Part 1: ', solution_part1('data/input.txt'))
