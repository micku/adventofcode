#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""

    return sum([int(x) for x in _input.split()])


def part2(_input):
    """Part 2 solution implementation"""

    i = 0
    values = _input.split()

    current_frequency = 0
    found_frequencies = set()

    while(current_frequency not in found_frequencies):
        found_frequencies.add(current_frequency)
        current_frequency += int(values[i % len(values)])
        i += 1

    return current_frequency


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = open(input_path, 'r').read().strip()

    print('Part 1 solution: {}'.format(part1(_input) or 'not solved :('))
    part2_solution = part2(_input)
    print('Part 2 solution: {}'.format(
        part2_solution if part2_solution is not None else 'nope.')
    )
