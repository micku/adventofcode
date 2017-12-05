#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""

    data = list(_input)
    i = 0
    cnt = 0

    while 0 <= i < len(data):
        cnt += 1
        data[i] += 1
        i += data[i] - 1

    return cnt


def part2(_input):
    """Part 2 solution implementation"""

    data = list(_input)
    i = 0
    cnt = 0

    while 0 <= i < len(data):
        cnt += 1
        incr = 1 if data[i] < 3 else -1
        data[i] += incr
        i += data[i] - incr

    return cnt


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = [int(x) for x in open(input_path, 'r').read().strip().split('\n')]

    print('Part 1 solution: {}'.format(part1(_input) or 'not solved :('))
    print('Part 2 solution: {}'.format(part2(_input) or 'nope.'))
