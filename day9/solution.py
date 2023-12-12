# https://adventofcode.com/2023/day/9
import os


def read_input(filename: str) -> (str, dict[str, (str, str)], list[str]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        result = []

        if len(raw_lines) == 0:
            return ()

        for raw_line in raw_lines:
            line = raw_line.rstrip()
            result.append([int(x) for x in line.split(' ')])

        return result


def step(inpt: list[list[int]]) -> list[list[int]]:
    if all(x == 0 for x in inpt[-1]):
        return inpt
    result = []
    for i in range(1, len(inpt[-1])):
        result.append(inpt[-1][i] - inpt[-1][i - 1])
    inpt.append(result)
    return step(inpt)


def result_step(steps: list[list[int]]) -> int:
    for r in range(len(steps) - 2, -1, -1):
        steps[r].append(steps[r][-1] + steps[r + 1][-1])
    return steps[0][-1]


def solution_part1(filename: str) -> int:
    nums = read_input(filename)
    result = 0
    for item in nums:
        result += result_step(step([item]))
    return result


def solution_part2(filename: str) -> int:
    nums = read_input(filename)
    result = 0
    for item in nums:
        result += result_step(step([item[::-1]]))
    return result


assert (solution_part2('data/input.test.txt') == 2)
print('Result Part 2: ', solution_part2('data/input.txt'))

assert (solution_part1('data/input.test.txt') == 114)
print('Result Part 1: ', solution_part1('data/input.txt'))
