#! /usr/bin/env python

import click

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    direction = 0
    position = (0, 0)

    route = f.read().rstrip().split(', ')

    if part == '1':
        for instruction in route:
            direction += 1 if instruction[0] == 'R' else -1
            distance = int(instruction[1:])
            position = (
                position[0] + (directions[direction%4][0] * distance),
                position[1] + (directions[direction%4][1] * distance)
            )
        print(sum([abs(x) for x in position]))

    if part == '2':
        positions_history = []
        for instruction in route:
            direction += 1 if instruction[0] == 'R' else -1
            distance = int(instruction[1:])

            for p in xrange(0, distance):
                position = (
                    position[0] + directions[direction%4][0],
                    position[1] + directions[direction%4][1]
                )
                if position in positions_history:
                    print(sum([abs(x) for x in position]))
                    return
                positions_history.append(position)


if __name__ == '__main__':
    run()
