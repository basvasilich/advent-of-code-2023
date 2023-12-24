# https://adventofcode.com/2023/day/16
import os


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = []

        if len(raw_lines) == 0:
            return ()

        for row, raw_line in enumerate(raw_lines):
            line = raw_line.rstrip()
            result.append([])
            for col, char in enumerate(line):
                result[row].append(char)

        return result


def calc_by_start(start: (int, int, str), m: list[list[str]]) -> int:
    visited = {}
    s = [start]

    while len(s) > 0:
        y, x, d = s.pop()

        if y > len(m) - 1 or x > len(m[0]) - 1 or y < 0 or x < 0 or (y, x) in visited and visited[(y, x)] == d:
            continue

        visited[(y, x)] = d
        char = m[y][x]

        if char == '.':
            if d == 'r':
                s.append((y, x + 1, d))
            elif d == 'l':
                s.append((y, x - 1, d))
            elif d == 'u':
                s.append((y - 1, x, d))
            elif d == 'd':
                s.append((y + 1, x, d))
        elif char == '-':
            if d == 'r':
                s.append((y, x + 1, d))
            elif d == 'l':
                s.append((y, x - 1, d))
            elif d == 'u' or d == 'd':
                s.append((y, x + 1, 'r'))
                s.append((y, x - 1, 'l'))
        elif char == '|':
            if d == 'r' or d == 'l':
                s.append((y - 1, x, 'u'))
                s.append((y + 1, x, 'd'))
            elif d == 'u':
                s.append((y - 1, x, d))
            elif d == 'd':
                s.append((y + 1, x, d))
        elif char == '/':
            if d == 'r':
                s.append((y - 1, x, 'u'))
            elif d == 'l':
                s.append((y + 1, x, 'd'))
            elif d == 'u':
                s.append((y, x + 1, 'r'))
            elif d == 'd':
                s.append((y, x - 1, 'l'))
        elif char == '\\':
            if d == 'r':
                s.append((y + 1, x, 'd'))
            elif d == 'l':
                s.append((y - 1, x, 'u'))
            elif d == 'u':
                s.append((y, x - 1, 'l'))
            elif d == 'd':
                s.append((y, x + 1, 'r'))

    return len(visited.keys())


def solution_part1(filename: str) -> int:
    m = read_input(filename)

    return calc_by_start((0, 0, 'r'), m)


def solution_part2(filename: str) -> int:
    m = read_input(filename)
    result = 0

    for x in range(len(m[0])):
        result = max(result, calc_by_start((0, x, 'd'), m))
        result = max(result, calc_by_start((len(m) - 1, x, 'u'), m))

    for y in range(len(m)):
        result = max(result, calc_by_start((y, 0, 'r'), m))
        result = max(result, calc_by_start((y, len(m[0]) - 1, 'l'), m))

    return result


assert (solution_part1('data/input.test.txt') == 46)
print('Result Part 1: ', solution_part1('data/input.txt'))


assert (solution_part2('data/input.test.txt') == 51)
print('Result Part 2: ', solution_part2('data/input.txt'))
