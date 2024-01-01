# https://adventofcode.com/2023/day/21
import copy
import os


def read_input(filename: str) -> (list[list[int]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        m = []

        if len(raw_lines) == 0:
            return ()

        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            r = []
            for col, char in enumerate(line):
                if char == 'S':
                    start = (row, col)
                r.append(char)
            m.append(r)
            row += 1

        return m, start


def step(m, h):
    r = set()
    for y, x in h:
        if 0 <= x <= len(m[0]) - 1 and 0 <= y - 1 <= len(m) - 1 and m[y - 1][x] != '#':
            r.add((y - 1, x))
        if 0 <= x - 1 <= len(m[0]) - 1 and 0 <= y <= len(m) - 1 and m[y][x - 1] != '#':
            r.add((y, x - 1))
        if 0 <= x <= len(m[0]) - 1 and 0 <= y + 1 <= len(m) - 1 and m[y + 1][x] != '#':
            r.add((y + 1, x))
        if 0 <= x + 1 <= len(m[0]) - 1 and 0 <= y <= len(m) - 1 and m[y][x + 1] != '#':
            r.add((y, x + 1))

    return r, m


def make_map(m, h, filename: str):
    new_m = copy.deepcopy(m)
    result = ''
    for y, x in h:
        if new_m[y][x] != '#':
            new_m[y][x] = '0'
    for row in new_m:
        result += ''.join(row) + '\n'
    f = open(os.path.join(os.path.dirname(__file__), filename), 'w')
    f.write(result)
    f.close()


def solution_part1(filename: str, steps: int) -> int:
    m, start = read_input(filename)
    h = set([start])
    counter = 0
    while counter < steps:
        h, m = step(m, h)
        make_map(m, h, 'output/map.txt')
        counter += 1
    return len(h)


assert (solution_part1('data/input.test.txt', 6) == 16)
print('Result Part 1: ', solution_part1('data/input.txt', 64))
