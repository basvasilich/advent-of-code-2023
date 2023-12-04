# https://adventofcode.com/2023/day/3
import os
from typing import Dict


def read_input(filename: str) -> (Dict[str, int], list[(int, int)], list[(int, int)]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    coord_num_map = {}
    symbol_coord_list = []
    gears_coords = []

    if len(raw_lines) == 0:
        return ()

    for row, raw_line in enumerate(raw_lines):
        line = raw_line.rstrip()
        cur_num = ''
        cur_coords = []

        for col, char in enumerate(line):
            if char.isdigit():
                if cur_num == '':
                    cur_num = str(row) + '|' + str(col) + '@' + char
                else:
                    cur_num += char
                cur_coords.append((row, col))
                if col == len(line) - 1:
                    for coord in cur_coords:
                        coord_num_map[coord] = cur_num
            else:
                if cur_num != '':
                    for coord in cur_coords:
                        coord_num_map[coord] = cur_num

                if char != '.':
                    symbol_coord_list.append((row, col))
                    if char == '*':
                        gears_coords.append((row, col))
                cur_num = ''
                cur_coords = []
    return coord_num_map, symbol_coord_list, gears_coords


def check_coord(coord: (int, int), coord_num_map: Dict[str, int]) -> set[str]:
    row, col = coord
    result = set()
    r = range(row - 1, row + 2)
    c = range(col - 1, col + 2)
    for i in r:
        for j in c:
            if (i, j) in coord_num_map.keys():
                result.add(coord_num_map[(i, j)])

    return result


def solution_part1(filename: str) -> int:
    coord_num_map, symbol_coord_list, gears_coords = read_input(filename)
    result = set()

    for coord in symbol_coord_list:
        result.update(check_coord(coord, coord_num_map))

    val = sum([int(x.split('@')[1]) for x in result])

    return val


def solution_part2(filename: str) -> int:
    coord_num_map, symbol_coord_list, gears_coords = read_input(filename)
    val = 0
    for coord in gears_coords:
        nums = check_coord(coord, coord_num_map)
        if len(nums) == 2:
            v1, v2 = list(nums)
            val += int(v1.split('@')[1]) * int(v2.split('@')[1])

    return val


assert (solution_part2('data/input2.test.txt') == 6756)
assert (solution_part2('data/input.test.txt') == 467835)
print('Result Part 2: ', solution_part2('data/adventofcode.com_2023_day_3_input.txt'))

assert (solution_part1('data/input2.test.txt') == 925)
assert (solution_part1('data/input.test.txt') == 4390)
print('Result Part 1: ', solution_part1('data/adventofcode.com_2023_day_3_input.txt'))
