# https://adventofcode.com/2023/day/18
import os


def read_input(filename: str) -> list[(str, str, str)]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        moves = []
        if len(raw_lines) == 0:
            return ()

        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            moves.append(line.split(' '))
            row += 1

        return moves


def solution_part1(filename: str) -> int:
    moves = read_input(filename)
    cur_x = 0
    cur_y = 0
    vertices = []
    lines = []
    for d, val, _ in moves:
        if d == 'R':
            cur_x += int(val)
        elif d == 'L':
            cur_x -= int(val)
        elif d == 'U':
            cur_y -= int(val)
        elif d == 'D':
            cur_y += int(val)
        vertices.append((cur_x, cur_y))

    result = 0
    for i in range(len(vertices) - 1):
        result += abs(vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1])
    return result * 0.5


assert (solution_part1('data/input.test.txt') == 62)
print('Result Part 1: ', solution_part1('data/input.txt'))
