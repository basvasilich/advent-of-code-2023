# https://adventofcode.com/2023/day/2
import os
import re


def read_input(filename: str) -> list[(int, list[(int, int, int)])]:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    result = []

    if len(raw_lines) == 0:
        return result

    for raw_line in raw_lines:
        line = raw_line.rstrip()
        card_prefix, card_data = line.split(':')
        card_id = int(re.sub(r'\D', '', card_prefix))
        card_numbers = card_data.split('|')
        winning_numbers = card_numbers[0].strip().split(' ')
        my_numbers = card_numbers[1].strip().split(' ')
        result.append((card_id, winning_numbers, my_numbers))

    return result


def solution_part1(filename: str) -> int:
    cards = read_input(filename)
    result = 0

    for card_id, winning_numbers, my_numbers in cards:
        count = 0
        for num in winning_numbers:
            if num in my_numbers:
                count += 1
        if count > 0:
            result += pow(2, count - 1)

    return result


# assert (solution_part2('data/input.test.txt') == 467835)
# print('Result Part 2: ', solution_part2('data/adventofcode.com_2023_day_3_input.txt'))

assert (solution_part1('data/input.test.txt') == 13)
print('Result Part 1: ', solution_part1('data/adventofcode.com_2023_day_4_input.txt'))
