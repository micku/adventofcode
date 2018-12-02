#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""

    return None


def part2(_input):
    """Part 2 solution implementation"""

    return None


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = open(input_path, 'r').read().strip()

    print('Part 1 solution: {}'.format(part1(_input) or 'not solved :('))
    print('Part 2 solution: {}'.format(part2(_input) or 'nope.'))
