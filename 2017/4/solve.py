#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""

    return len([p for p in _input if is_passphrase_valid(p.split(' '))])


def part2(_input):
    """Part 2 solution implementation"""

    return len([p for p in _input if is_passphrase_valid_v2(p.split(' '))])


def is_passphrase_valid(passphrase):
    return len(passphrase) == len(set(passphrase))


def is_passphrase_valid_v2(passphrase):
    sorted_pass = [''.join(sorted(w)) for w in passphrase]
    return len(sorted_pass) == len(set(sorted_pass))


if __name__ == '__main__':
    input_path = os.path.join(
        os.path.dirname(__file__),
        'input')
    _input = open(input_path, 'r').read().strip().split('\n')

    print('Part 1 solution: {}'.format(part1(_input) or 'not solved :('))
    print('Part 2 solution: {}'.format(part2(_input) or 'nope.'))
