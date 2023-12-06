# https://adventofcode.com/2023/day/5
import os
import re


def read_input(filename: str):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
    seeds = []
    maps = []
    limits = []
    cur_map = None

    if len(raw_lines) == 0:
        return ()

    i = 0
    while i < len(raw_lines):
        line = raw_lines[i].rstrip()

        if i == 0:
            seeds = [int(x) for x in re.sub(r'seeds: ', '', re.sub(r'\s+', ' ', line)).split(' ')]
            i += 1
        elif line == '':
            if cur_map:
                maps[-1] = sorted(cur_map, key=lambda x: x[1] + x[2])
                limits.append((min([x[1] for x in maps[-1]]), max([x[1] + x[2] for x in maps[-1]])))
            maps.append([])
            cur_map = maps[-1]
            i += 2
        else:
            cur_map.append([int(x) for x in re.sub(r'\s+', ' ', line).split(' ')])
            i += 1

    limits.append((min([x[1] for x in maps[-1]]), max([x[1] + x[2] for x in maps[-1]])))

    return seeds, maps, limits


def apply_map(val, to_map):
    for dst, source, delta in to_map:
        if source <= val < (source + delta):
            return dst + val - source
    return val


def solution_part1(filename: str) -> int:
    seeds, maps, limits = read_input(filename)
    result = 10**1000

    for seed in seeds:
        val = seed
        for i, to_map in enumerate(maps):
            if limits[i][0] <= val <= limits[i][1]:
                val = apply_map(val, to_map)
        result = min(val, result)

    return result


def solution_part2(filename: str) -> int:
    seeds, maps, limits = read_input(filename)
    pairs = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
    result = 10**1000

    for s, l in pairs:
        for seed in range(s, s + l + 1):
            val = seed
            for i, to_map in enumerate(maps):
                if limits[i][0] <= val <= limits[i][1]:
                    val = apply_map(val, to_map)
            result = min(val, result)

    return result


assert (solution_part1('data/input.test.txt') == 35)
print('Result Part 1: ', solution_part1('data/input.txt'))

assert (solution_part2('data/input.test.txt') == 46)
print('Result Part 2: ', solution_part2('data/input.txt'))
