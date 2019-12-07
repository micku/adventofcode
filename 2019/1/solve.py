"""Solution to the AoC problem"""

import math
import os

from yaspin import yaspin


def part1(_input):
    """Part 1 solution implementation"""

    return sum([math.floor(int(x) / 3) - 2 for x in _input.split()])


def part2(_input):
    """Part 2 solution implementation"""

    return sum([fuel_req(x) for x in _input.split()])

def fuel_req(mass: int) -> int:
    req = math.floor(int(mass) / 3 - 2)

    if req > 0:
        req += fuel_req(req)

    return req if req > 0 else 0


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input')
    with yaspin(text=f'Reading the input file') as spinner:
        _input = open(input_path, 'r').read().strip()
        spinner.ok("✔ ")

    for i in range(1, 3):
        with yaspin(text=f'Solving part {i}...') as spinner:
            solution = locals()[f'part{i}'](_input)

            if solution is None:
                spinner.fail("✘ ")
            else:
                spinner.ok("✔ ")
                print(f'  Solution is: {solution}')
