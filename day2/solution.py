# https://adventofcode.com/2023/day/1
import os
import re

constraints = {'red': 12, 'green': 13, 'blue': 14}


def read_input(filename: str) -> list[(int, list[(int, int, int)])]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    result = []

    if len(raw_lines) == 0:
        return result

    for raw_line in raw_lines:
        line = raw_line.rstrip()
        game_prefix, game_data = line.split(':')
        game_number = int(re.sub(r'\D', '', game_prefix))
        game_moves = game_data.split(';')
        game_result = list(map(lambda move: [x.strip().split(' ') for x in move.split(',')], game_moves))
        result.append((game_number, game_result))

    return result


def solution_part1(filename: str) -> int:
    games = read_input(filename)
    result = 0
    for game_number, game_moves in games:
        is_game_possible = True
        for move in game_moves:
            for gems_num, gems_key in move:
                if constraints[gems_key] < int(gems_num):
                    is_game_possible = False
                    break

        if is_game_possible:
            result += game_number

    return result


def solution_part2(filename: str) -> int:
    games = read_input(filename)
    result = 0
    for game_number, game_moves in games:
        powers = {'red': 0, 'green': 0, 'blue': 0}
        for move in game_moves:
            for gems_num, gems_key in move:
                powers[gems_key] = max(powers[gems_key], int(gems_num))

        result += powers['red'] * powers['green'] * powers['blue']

    return result


assert (solution_part1('data/input.test.txt') == 8)
print('Result Part 1: ', solution_part1('data/adventofcode.com_2023_day_2_input.txt'))

assert (solution_part2('data/input.test.txt') == 2286)
print('Result Part 1: ', solution_part2('data/adventofcode.com_2023_day_2_input.txt'))
