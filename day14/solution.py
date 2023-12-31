# https://adventofcode.com/2023/day/14
import os
import copy


def read_input(filename: str) -> (list[list[str]], (int, int)):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = [[''] * len(raw_lines) for _ in range(len(raw_lines[0].rstrip()))]

        if len(raw_lines) == 0:
            return ()

        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            for col, char in enumerate(line):
                if char != '.':
                    result[row][col] = char
            row += 1

        return result


def tilt(row: list[str]) -> list[str]:
    point_r = 0
    point_w = 0
    new_row = copy.deepcopy(row)
    while point_r < len(row):
        char = row[point_r]
        if char == '#' and point_r < len(row):
            point_w = point_r + 1
        elif char == 'O':
            new_row[point_r] = ''
            new_row[point_w] = 'O'
            point_w += 1
        point_r += 1
    return new_row


def get_sum(matrix: list[list[str]]) -> int:
    result = 0
    for index, row in enumerate(matrix):
        for char in row:
            if char == 'O':
                result += len(matrix) - index
    return result


def tilt_to_n(matrix: list[list[str]]) -> list[list[str]]:
    new_matrix = copy.deepcopy(matrix)

    for col in range(len(matrix[0])):
        new_col_arr = []
        for row in range(len(matrix)):
            new_col_arr.append(matrix[row][col])
        new_col_arr = tilt(new_col_arr)
        for row in range(len(matrix)):
            new_matrix[row][col] = new_col_arr[row]
    return new_matrix


def tilt_to_w(matrix: list[list[str]]) -> list[list[str]]:
    new_matrix = copy.deepcopy(matrix)

    for row in range(len(matrix)):
        new_col_arr = []
        for col in range(len(matrix[0])):
            new_col_arr.append(matrix[row][col])
        new_col_arr = tilt(new_col_arr)
        for col in range(len(matrix[0])):
            new_matrix[row][col] = new_col_arr[col]
    return new_matrix


def tilt_to_e(matrix: list[list[str]]) -> list[list[str]]:
    new_matrix = copy.deepcopy(matrix)

    for row in range(len(matrix)):
        new_col_arr = []
        for col in range(len(matrix[0]) - 1, -1, -1):
            new_col_arr.append(matrix[row][col])
        new_col_arr = tilt(new_col_arr)[::-1]
        for col in range(len(matrix[0])):
            new_matrix[row][col] = new_col_arr[col]
    return new_matrix


def tilt_to_s(matrix: list[list[str]]) -> list[list[str]]:
    new_matrix = copy.deepcopy(matrix)

    for col in range(len(matrix[0])):
        new_col_arr = []
        for row in range(len(matrix) - 1, -1, -1):
            new_col_arr.append(matrix[row][col])
        new_col_arr = tilt(new_col_arr)[::-1]
        for row in range(len(matrix)):
            new_matrix[row][col] = new_col_arr[row]
    return new_matrix


def solution_part1(filename: str) -> int:
    m = read_input(filename)
    m = tilt_to_n(m)

    return get_sum(m)


def circle(matrix: list[list[str]]) -> list[list[str]]:
    new_matrix = copy.deepcopy(matrix)
    new_matrix = tilt_to_n(new_matrix)
    new_matrix = tilt_to_w(new_matrix)
    new_matrix = tilt_to_s(new_matrix)
    new_matrix = tilt_to_e(new_matrix)
    return new_matrix


def guess_seq_len(seq):
    new_seq = seq[::-1]
    guess = 1
    max_len = len(new_seq) // 2
    for x in range(2, max_len):
        if new_seq[0:x] == new_seq[x:2 * x] == new_seq[2 * x:3 * x] == new_seq[3 * x:4 * x]:
            return x, len(new_seq) - 4 * x

    return guess, len(new_seq)


def encode_matrix(matrix: list[list[str]]) -> str:
    result = ''
    for row in range(len(matrix)):
        result += str(matrix[row])
    return result


def solution_part2(filename: str) -> int:
    m = read_input(filename)
    sums_by_count = []
    count = 0
    while count < 1000000000:
        m = circle(m)
        sums_by_count.append((encode_matrix(m), get_sum(m)))
        guess_len, start_len = guess_seq_len(sums_by_count)
        index_in_circle = guess_len - (1000000000 - start_len) % guess_len
        if guess_len > 1:
            return sums_by_count[guess_len + start_len - index_in_circle - 1][1]
        count += 1

    return get_sum(m)


assert (solution_part1('data/input.test.txt') == 136)
print('Result Part 1: ', solution_part1('data/input.txt'))

assert (solution_part2('data/input.test.txt') == 64)
print('Result Part 2: ', solution_part2('data/input.txt'))
