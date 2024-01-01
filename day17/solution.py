# https://adventofcode.com/2023/day/17
import os


def read_input(filename: str) -> list[list[int]]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        m = []

        if len(raw_lines) == 0:
            return []

        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            m.append([int(x) for x in line])

        return m


def solution_part1(filename: str) -> int:
    m = read_input(filename)
    l_row = len(m)
    l_col = len(m[0])
    dp = [[10000000000000] * l_col for _ in range(l_row)]
    for i in range(1, l_row):
        dp[i][0] = dp[i - 1][0] + m[i][0]
    for j in range(1, l_col):
        dp[0][j] = dp[0][j - 1] + m[0][j]
    for i in range(1, l_row):
        for j in range(1, l_col):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + m[i][j]

    result = dp[l_row - 1][l_col - 1]

    return result



assert (solution_part1('data/input.test.txt') == 19114)
print('Result Part 1: ', solution_part1('data/input.txt'))
