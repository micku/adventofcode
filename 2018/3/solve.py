#! /usr/bin/env python
"""Solution to the AoC problem"""

import os


def part1(_input):
    """Part 1 solution implementation"""

    import re

    r = re.compile("#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

    overlapped = set()
    fabric = set()

    for claim in _input.split("\n"):
        offset_left, offset_top, width, height = (int(x) for x in r.match(claim).groups())
        for w in range(width):
            for h in range(height):
                square = f"{offset_left+w}-{offset_top+h}"
                if square in fabric:
                    overlapped.add(square)
                fabric.add(square)

    return len(overlapped)


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
