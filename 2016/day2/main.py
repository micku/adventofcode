#! /usr/bin/env python

import click
import operator

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    keypad = None
    position = None
    directions = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0),
    }

    if part == '1':
        keypad = {
            (0, 0): 1, (1, 0): 2, (2, 0): 3,
            (0, 1): 4, (1, 1): 5, (2, 1): 6,
            (0, 2): 7, (1, 2): 8, (2, 2): 9,
        }
        position = (1, 1)

    if part == '2':
        keypad = {
                                    (2, 0): 1,
                       (1, 1): 2,   (2, 1): 3,   (3, 1): 4,
            (0, 2): 5, (1, 2): 6,   (2, 2): 7,   (3, 2): 8,   (4, 2): 9,
                       (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
                                    (2, 4): 'D',
        }
        position = (0, 2)

    for number_procedure in f:
        for instruction in number_procedure.rstrip():
            new_position = tuple(map(
                operator.add,
                position,
                directions[instruction]))
            if new_position in keypad.keys():
                position = new_position
        click.echo(keypad[position], nl=False)
    click.echo('')


if __name__ == '__main__':
    run()
