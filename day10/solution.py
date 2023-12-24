# https://adventofcode.com/2023/day/10
import os


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = []
        start = ()

        if len(raw_lines) == 0:
            return ()

        for row, raw_line in enumerate(raw_lines):
            line = raw_line.rstrip()
            result.append([])
            for col, char in enumerate(line):
                if char == 'S':
                    start = (row, col)
                result[row].append(char)

        return result, start


def step(inp: list[list[str]], cell: (int, int), path: list[(int, int, str)]):
    st = [cell]

    while len(st):
        row, col = st.pop()

        if row > len(inp) - 1 or row < 0 or col > len(inp[0]) - 1 or col < 0:
            continue
        char = inp[row][col]

        if char == 'S':
            path.append((row, col, char))
            return path

        if char == '.':
            continue

        last_row, last_col, last_char = path[-1]

        if char == '|':
            if last_row < row and last_col == col:
                path.append((row, col, char))

                st.append((row + 1, col))
            elif last_col == col:
                path.append((row, col, char))
                st.append((row - 1, col))

        if char == '-':
            if last_row == row and last_col < col:
                path.append((row, col, char))
                st.append((row, col + 1))
            elif last_row == row:
                path.append((row, col, char))
                st.append((row, col - 1))

        if char == 'L':
            if last_row < row and last_col == col:
                path.append((row, col, char))
                st.append((row, col + 1))
            elif last_row == row and last_col > col:
                path.append((row, col, char))
                st.append((row - 1, col))

        if char == 'J':
            if last_row == row and last_col < col:
                path.append((row, col, char))
                st.append((row - 1, col))
            elif last_row < row and last_col == col:
                path.append((row, col, char))
                st.append((row, col - 1))

        if char == '7':
            if last_row == row and last_col < col:
                path.append((row, col, char))
                st.append((row + 1, col))
            elif last_row > row and last_col == col:
                path.append((row, col, char))
                st.append((row, col - 1))

        if char == 'F':
            if last_row > row and last_col == col:
                path.append((row, col, char))
                st.append((row, col + 1))
            elif last_row == row and last_col > col:
                path.append((row, col, char))
                st.append((row + 1, col))

    return path


def check_path(path: list[(int, int, str)]) -> bool:
    for row, col, char in path:
        if char == 'S':
            return True
    return False


def solution_part1(filename: str) -> int:
    inp, start = read_input(filename)
    row, col = start
    path_t = step(inp, (row - 1, col), [(row, col, '')])
    if check_path(path_t):
        return len(path_t) // 2

    path_b = step(inp, (row + 1, col), [(row, col, '')])
    if check_path(path_b):
        return len(path_b) // 2

    path_l = step(inp, (row, col - 1), [(row, col, '')])
    if check_path(path_l):
        return len(path_l) // 2

    path_r = step(inp, (row, col + 1), [(row, col, '')])
    if check_path(path_r):
        return len(path_r) // 2

    return 0


def check_point_by_ray(point: (int, int), borders: set[(int, int)], mid_col: int, len_inp: int):
    row, col = point
    count = 0
    if col >= mid_col:
        for i in range(col + 1, len_inp):
            if (row, i)  in borders:
                count += 1
    else:
        for i in range(col-1, -1, -1):
            if (row, i) in borders:
                count += 1
    return count % 2 == 1


def solution_part2(filename: str) -> int:
    inp, start = read_input(filename)
    row, col = start
    borders = set()
    counter = 0

    path_t = step(inp, (row - 1, col), [(row, col, '')])
    if check_path(path_t):
        for row, col, _ in path_t:
            borders.add((row, col))

    path_b = step(inp, (row + 1, col), [(row, col, '')])
    if check_path(path_b):
        for row, col, _ in path_b:
            borders.add((row, col))

    path_l = step(inp, (row, col - 1), [(row, col, '')])
    if check_path(path_l):
        for row, col, _ in path_l:
            borders.add((row, col))

    path_r = step(inp, (row, col + 1), [(row, col, '')])
    if check_path(path_r):
        for row, col, _ in path_r:
            borders.add((row, col))

    for row in range(len(inp)):
        for col in range(len(inp[0])):
            if (row, col) not in borders and check_point_by_ray((row, col), borders, len(inp[0]) // 2, len(inp[00])):
                counter += 1

    return counter


assert (solution_part2('data/input5.test.txt') == 4)
assert (solution_part2('data/input3.test.txt') == 10)
assert (solution_part2('data/input4.test.txt') == 8)
print('Result Part 2: ', solution_part1('data/input.txt'))

assert (solution_part1('data/input2.test.txt') == 8)
assert (solution_part1('data/input.test.txt') == 4)
print('Result Part 1: ', solution_part1('data/input.txt'))
