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


def make_map(m, filename: str):
    result = ''
    for row in m:
        result += ''.join(row) + '\n'
    f = open(os.path.join(os.path.dirname(__file__), filename), 'w')
    f.write(result)
    f.close()


def bfs(m, start):
    h = [start]

    while len(h):
        y, x = h.pop()

        if x == 0 or x == len(m[0]) - 1 or y == 0 or y == len(m):
            continue

        if m[y][x] == '.':
            m[y][x] = 'I'
            h.append((y - 1, x))
            h.append((y, x - 1))
            h.append((y + 1, x))
            h.append((y, x + 1))
    return m


def solution_part1(filename: str) -> int:
    moves = read_input(filename)
    cur_x = 0
    cur_y = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    vertices = [(cur_x, cur_y)]
    for d, val, _ in moves:
        if d == 'R':
            cur_x += int(val)
        elif d == 'L':
            cur_x -= int(val)
        elif d == 'U':
            cur_y -= int(val)
        elif d == 'D':
            cur_y += int(val)
        max_x = max(max_x, cur_x)
        min_x = min(min_x, cur_x)
        max_y = max(max_y, cur_y)
        min_y = min(min_y, cur_y)
        vertices.append((cur_x, cur_y))

    m = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for i in range(1, len(vertices)):
        x1, y1 = vertices[i - 1]
        x2, y2 = vertices[i]
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                m[y - min_y][x - min_x] = '#'

    make_map(m, 'output/perimetr.txt')

    if len(m[0]) < 200:
        m = bfs(m, (1, 1))
    else:
        m = bfs(m, (1, 295))

    make_map(m, 'output/interior.txt')

    counter = 0
    for y in range(len(m)):
        for x in range(len(m[0])):
            char = m[y][x]
            if char == '#' or char == 'I':
                counter += 1
    return counter


assert (solution_part1('data/input.test.txt') == 62)
print('Result Part 1: ', solution_part1('data/input.txt'))
