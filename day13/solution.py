# https://adventofcode.com/2023/day/11
import os


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = []

        if len(raw_lines) == 0:
            return ()

        row = 0
        curr_part = []
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            if line == '':
                result.append(curr_part)
                curr_part = []
            else:
                curr_part.append(line)
            row += 1
        result.append(curr_part)

        return result


def check_hor_line(part: list[str]) -> int:
    rows = []
    for row in range(1, len(part) - 2):
        pointer_s = row - 1
        pointer_e = row
        is_valid = True
        while pointer_s >= 0 and pointer_e < len(part):
            if part[pointer_s] != part[pointer_e]:
                is_valid = False
                break
            pointer_s -= 1
            pointer_e += 1
        if is_valid:
            rows.append(row)

    return max(rows) if len(rows) > 0 else 0


def check_vert_line(part: list[str]) -> int:
    cols = []
    for col in range(1, len(part[0]) - 2):
        is_valid = True
        for row in range(len(part)):
            l = min(col, len(part[0]) - col)
            part_l = part[row][col - l:col][::-1]
            part_r = part[row][col:col + l]
            if part_l != part_r:
                is_valid = False
                break
        if is_valid:
            cols.append(col)

    return max(cols) if len(cols) > 0 else 0


def solution_part1(filename: str) -> int:
    parts = read_input(filename)
    sum = 0
    for part in parts:
        row = check_hor_line(part)
        col = check_vert_line(part)
        sum += row * 100 + col
    return sum


assert (solution_part1('data/input3.test.txt') == 3)
assert (solution_part1('data/input2.test.txt') == 709)
assert (solution_part1('data/input.test.txt') == 405)
print('Result Part 1: ', solution_part1('data/input.txt'))
