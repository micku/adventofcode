#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""

    data = list(_input)
    data_len = len(data)

    redistr = set([''.join(str(x) for x in data)])

    cnt = 0
    while True:
        cnt += 1
        max_value = max(data)
        max_index = data.index(max_value)

        for i in range(max_value + 1):
            idx = i + max_index
            data[idx % data_len] = data[idx % data_len] + 1 if i else 0

        str_data = '-'.join(str(x) for x in data)

        if str_data in redistr:
            break

        redistr.add(str_data)

    return cnt


def part2(_input):
    """Part 2 solution implementation"""

    data = list(_input)
    data_len = len(data)

    redistr = set([''.join(str(x) for x in data)])

    cnt = 0
    seen = False
    seen_redistr = ''
    seen_count = 0
    while True:
        cnt += 1
        max_value = max(data)
        max_index = data.index(max_value)

        for i in range(max_value + 1):
            idx = i + max_index
            data[idx % data_len] = data[idx % data_len] + 1 if i else 0

        str_data = '-'.join(str(x) for x in data)

        if seen:
            if seen_redistr == str_data:
                break

        if not seen and str_data in redistr:
            seen_redistr = str_data
            seen_count = cnt
            seen = True

        redistr.add(str_data)

    return cnt - seen_count


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = [int(x) for x in open(input_path, 'r').read().strip().split('\t')]

    print('Part 1 solution: {}'.format(part1(_input) or 'not solved :('))
    print('Part 2 solution: {}'.format(part2(_input) or 'nope.'))
