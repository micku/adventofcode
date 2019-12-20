"""Solution to the AoC problem"""

import os

from yaspin import yaspin


def part1(_input):
    """Part 1 solution implementation"""

    length = 6
    (lbound, ubound) = map(int, _input.split('-'))

    return len([x for x in range(lbound, ubound) if valid_password(str(x))])


def part2(_input):
    """Part 2 solution implementation"""

    return None


def valid_password(password: str) -> bool:
    doubles = 0
    for x in range(0, len(password) -1):
        if password[x] == password[x + 1]:
            doubles += 1

        if password[x] > password[x + 1]:
            return False

    return doubles > 0


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input')
    with yaspin(text=f'Reading the input file') as spinner:
        _input = '172930-683082'
        spinner.ok("✔ ")

    for i in range(1, 3):
        with yaspin(text=f'Solving part {i}...') as spinner:
            solution = locals()[f'part{i}'](_input)

            if solution is None:
                spinner.fail("✘ ")
            else:
                spinner.ok("✔ ")
                print(f'  Solution is: {solution}')
