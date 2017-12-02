#! /usr/bin/env python
"""Solution to the AoC problem"""

import os
import itertools


def part1(_input):
    """Part 1 solution implementation"""

    return sum(max(row) - min(row) for row in _input)


def part2(_input):
    """Part 2 solution implementation"""

    return int(sum(next(
        max(val) / min(val) for val in itertools.combinations(row, 2) if max(val) % min(val) == 0
        ) for row in _input))


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = open(input_path, 'r').read().strip()

    _input = [[int(val) for val in row.split('\t')] for row in _input.split('\n')]

    print('Part 1 solution: {}'.format(part1(_input) or 'not solved :('))
    print('Part 2 solution: {}'.format(part2(_input) or 'nope.'))
