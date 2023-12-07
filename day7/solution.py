# https://adventofcode.com/2023/day/7
import os
import re
from collections import Counter
from heapq import heappush, heappop

cards_rank = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '#')


def make_list_of_values_with_copy(cards_counter: Counter) -> (list[int], list[int]):
    val = list(cards_counter.values())
    cards_counter_copy = cards_counter.copy()
    cards_counter_copy.pop('#', None)
    val_copy = list(cards_counter_copy.values())
    return val, val_copy


def high_card_check(cards_counter: Counter) -> bool:
    val = list(cards_counter.values())
    return val[0] == val[1] == val[2] == val[3] == val[4] == 1


def one_pair_check(cards_counter: Counter) -> bool:
    val = list(cards_counter.values())
    if 2 in val:
        return True
    if cards_counter['#'] == 1:
        return True
    return False


def two_pair_check(cards_counter: Counter) -> bool:
    val, val_copy = make_list_of_values_with_copy(cards_counter)
    count = 0
    for x in val:
        if x == 2:
            count += 1
    if count == 2:
        return True
    if cards_counter['#'] == 1 and 2 in val_copy:
        return True
    return False


def three_of_a_kind_check(cards_counter: Counter) -> bool:
    val, val_copy = make_list_of_values_with_copy(cards_counter)
    if 3 in val:
        return True
    if cards_counter['#'] == 1 and 2 in val_copy:
        return True
    if cards_counter['#'] >= 2:
        return True
    return False


def full_house_check(cards_counter: Counter) -> bool:
    val, val_copy = make_list_of_values_with_copy(cards_counter)
    count = 0
    for x in val:
        if x == 2:
            count += 1

    if 2 in val and 3 in val:
        return True
    if cards_counter['#'] == 1 and count == 2:
        return True
    if cards_counter['#'] >= 2 and 2 in val_copy:
        return True
    return False


def four_of_a_kind_check(cards_counter: Counter) -> bool:
    val, val_copy = make_list_of_values_with_copy(cards_counter)
    if 4 in val:
        return True
    if cards_counter['#'] == 1 and 3 in val_copy:
        return True
    if cards_counter['#'] == 2 and 2 in val_copy:
        return True
    if cards_counter['#'] >= 3:
        return True
    return False


def five_of_a_kind_check(cards_counter: Counter) -> bool:
    val, val_copy = make_list_of_values_with_copy(cards_counter)
    if 5 in val:
        return True
    if cards_counter['#'] == 1 and 4 in val_copy:
        return True
    if cards_counter['#'] == 2 and 3 in val_copy:
        return True
    if cards_counter['#'] == 3 and 2 in val_copy:
        return True
    if cards_counter['#'] >= 4:
        return True
    return False


def get_rank(cards: str) -> int:
    cards_counter = Counter(cards)

    if five_of_a_kind_check(cards_counter):
        return 1000

    if four_of_a_kind_check(cards_counter):
        return 2000

    if full_house_check(cards_counter):
        return 3000

    if three_of_a_kind_check(cards_counter):
        return 4000

    if two_pair_check(cards_counter):
        return 5000

    if one_pair_check(cards_counter):
        return 6000

    if high_card_check(cards_counter):
        return 7000


def read_input(filename: str) -> (str, int):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    result = []

    if len(raw_lines) == 0:
        return result

    for raw_line in raw_lines:
        line = raw_line.rstrip()
        cards, bid = line.split(' ')
        result.append((cards, int(bid)))

    return result


def custom_sort(strings):
    return sorted(strings, key=lambda x: [cards_rank.index(c) for c in x[0]])


def make_solution(items: list, is_part2: bool = False) -> int:
    ranks = {}
    h = []
    result = 0

    for cards, bid in items:

        if is_part2:
            cards = re.sub(r"J", '#', cards)
        rank = get_rank(cards)
        if rank in ranks.keys():
            ranks[rank].append((cards, bid))
        else:
            ranks[rank] = [(cards, bid)]

    for key in ranks.keys():
        ranks[key] = custom_sort(ranks[key])
        for index, item in enumerate(ranks[key]):
            heappush(h, (-1 * (key + index), item))

    counter = 1
    while len(h):
        index, (cards, bid) = heappop(h)
        result += counter * bid
        counter += 1
    return result


def solution_part1(filename: str) -> int:
    items = read_input(filename)
    return make_solution(items)


def solution_part2(filename: str) -> int:
    items = read_input(filename)
    return make_solution(items, True)


assert (solution_part2('data/input2.test.txt') == 6839)
assert (solution_part2('data/input.test.txt') == 5905)
print('Result Part 2: ', solution_part2('data/input.txt'))

assert (solution_part1('data/input2.test.txt') == 6592)
assert (solution_part1('data/input.test.txt') == 6440)
print('Result Part 1: ', solution_part1('data/input.txt'))
