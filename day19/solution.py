# https://adventofcode.com/2023/day/16
import os


def read_input(filename: str) -> (dict[str, dict[str, list[(str, int, str)]]], dict[str, int]):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        raw_lines = file.readlines()
        tree = {}
        parts = []

        if len(raw_lines) == 0:
            return ()

        is_read_parts = False
        row = 0
        while row < len(raw_lines):
            line = raw_lines[row].rstrip()
            if line == '':
                is_read_parts = True
            elif is_read_parts:
                parts.append(dict(item.split('=') for item in line.strip('{}').split(',')))
            else:
                s1 = line.split('{')
                key = s1[0]
                tree[key] = {
                    'items': [],
                    'last': ''
                }
                conds = s1[1].strip('{}').split(',')
                for index, cond in enumerate(conds):
                    if index == len(conds) - 1:
                        tree[key]['last'] = cond
                    else:
                        cond_arr = cond.split(':')
                        cond_next = cond_arr[1]
                        if '>' in cond:
                            cond_exp = '>'

                        elif '<':
                            cond_exp = '<'
                        cond_key, cond_val = cond_arr[0].split(cond_exp)
                        tree[key]['items'].append((cond_key, cond_exp, int(cond_val), cond_next))

            row += 1
        return tree, parts


def solution_part1(filename: str) -> int:
    tree, parts = read_input(filename)
    result = 0
    for part in parts:
        cur_step_key = 'in'
        while cur_step_key != 'A' and cur_step_key != 'R':
            cur_step = tree[cur_step_key]
            is_some_cond = False
            for cond_key, cond_exp, cond_val, cond_next in cur_step['items']:
                part_val = int(part[cond_key])
                if cond_exp == '>':
                    if part_val > cond_val:
                        is_some_cond = True
                        cur_step_key = cond_next
                        break
                elif cond_exp == '<':
                    if part_val < cond_val:
                        is_some_cond = True
                        cur_step_key = cond_next
                        break
            if not is_some_cond:
                cur_step_key = cur_step['last']
        if cur_step_key == 'A':
            result += sum([int(x) for x in part.values()])
    return result


assert (solution_part1('data/input.test.txt') == 19114)
print('Result Part 1: ', solution_part1('data/input.txt'))
