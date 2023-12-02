# https://adventofcode.com/2023/day/1
import os

digits = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'),
          ('eight', '8'), ('nine', '9')]

reverse_digits = [(x[0][::-1], x[1]) for x in digits]


def make_digits_hashtable(input_digits: list):
    result = {}
    for digit in input_digits:
        if digit[0][0] in result.keys():
            result[digit[0][0]].append(digit)
        else:
            result[digit[0][0]] = [digit]
    return result


from_start_digits = make_digits_hashtable(digits)
from_end_digits = make_digits_hashtable(reverse_digits)


def find_first_digit(input_string: str, input_digits: dict) -> str:
    pointer = 0
    while pointer < len(input_string):
        char = input_string[pointer]
        if char.isdigit():
            return char

        if len(input_digits.keys()) > 0 and char in input_digits.keys():
            for k, val in input_digits[char]:
                if len(k) > len(input_string[pointer::]):
                    continue
                lp_k = input_string[pointer:pointer + len(k):]
                if lp_k == k:
                    return str(val)
        pointer += 1


def make_solution(filename: str, forward_digits: dict, reverse_digits) -> int:
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()

    if len(raw_lines) == 0:
        return 0

    cur_sum = 0

    for raw_line in raw_lines:
        line = raw_line.rstrip()
        reverse_line = line[::-1]
        cur_sum += int(find_first_digit(line, forward_digits) + find_first_digit(reverse_line, reverse_digits))

    return cur_sum


def solution_part1(filename: str) -> int:
    return make_solution(filename, {}, {})


def solution_part2(filename: str) -> int:
    return make_solution(filename, from_start_digits, from_end_digits)


assert (solution_part1('data/input.test.txt') == 142)
print('Result Part 1: ', solution_part1('data/adventofcode.com_2023_day_1_input.txt'))
assert (solution_part2('data/input2.test.txt') == 281)
print('Result Part 2: ', solution_part2('data/adventofcode.com_2023_day_1_input.txt'))
