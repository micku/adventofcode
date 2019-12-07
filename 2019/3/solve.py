"""Solution to the AoC problem"""

import os

from yaspin import yaspin


def part1(_input):
    """Part 1 solution implementation"""

    start = (0, 0)
    paths = parse_input(_input)

    (coords_wire1, _) = calculate_coords(paths[0])
    (coords_wire2, _) = calculate_coords(paths[1])

    intersections = coords_wire1 & coords_wire2

    return min([distance(start, b) for b in intersections])


def part2(_input):
    """Part 2 solution implementation"""

    start = (0, 0)
    paths = parse_input(_input)

    (coords_wire1, total_steps1) = calculate_coords(paths[0])
    (coords_wire2, total_steps2) = calculate_coords(paths[1])

    intersections = coords_wire1 & coords_wire2

    return min([
        total_steps1[b] + total_steps2[b] for b in intersections
    ])


def distance(a, b):
    """Calculates the Manhattan Distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_input(_input):
    return [x.split(',') for x in _input.split()]


def calculate_coords(path):
    position = [0, 0]
    coords = set()
    steps = 0
    total_steps = {}

    for m in path:
        direction = m[0]
        distance = int(m[1:])

        """Add if going right or up, subtract for down and left"""
        position_multiplier = 1 if direction in ['R', 'U'] else -1
        """Use X if going up or down, Y for left and right"""
        position_axis = 0 if direction in ['U', 'D'] else 1

        for x in range(distance):
            steps += 1
            position[position_axis] += position_multiplier
            coords.add(tuple(position))
            if tuple(position) not in total_steps:
                total_steps[tuple(position)] = steps

    return (coords, total_steps)

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
