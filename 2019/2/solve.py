"""Solution to the AoC problem"""

import math
import os

from copy import copy
from itertools import permutations

from yaspin import yaspin


OPS = {
    1: sum,
    2: math.prod,
}

def part1(_input):
    """Part 1 solution implementation"""

    prog = list(map(int, _input.split(',')))
    return execute(prog, 12, 2)


def part2(_input):
    """Part 2 solution implementation"""

    initial_memory = list(map(int, _input.split(',')))

    noun = 0
    verb = 0

    result = 19690720

    for x in permutations(range(100), 2):
        (noun, verb) = x
        prog = copy(initial_memory)
        if execute(prog, noun, verb) == result:
            return 100 * noun + verb


def execute(prog: list, noun: int, verb: int) -> list:
    prog[1] = noun
    prog[2] = verb
    for x in range(0, len(prog), 4):
        if prog[x] == 99:
            return prog[0]

        op = OPS[prog[x]]
        prog[prog[x + 3]] = op([prog[prog[x + 1]], prog[prog[x + 2]]])


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
