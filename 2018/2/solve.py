#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""
    counter = {2: 0, 3: 0}

    for id in _input.split():
        letters_count = ''.join([str(id.count(x)) for x in set(id)])
        counter[2] += 1 if letters_count.count("2") else 0
        counter[3] += 1 if letters_count.count("3") else 0

    return counter[2] * counter[3]


def part2(_input):
    """Part 2 solution implementation"""

    return None


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = open(input_path, 'r').read().strip()

    part1_solution = part1(_input)
    print('Part 1 solution: {}'.format(
        part1_solution if part1_solution is not None else 'nope.')
    )
    part2_solution = part2(_input)
    print('Part 2 solution: {}'.format(
        part2_solution if part2_solution is not None else 'nope.')
    )
