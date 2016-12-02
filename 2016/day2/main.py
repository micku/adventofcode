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
    keypad = {
        (0, 0): 1, (1, 0): 2, (2, 0): 3,
        (0, 1): 4, (1, 1): 5, (2, 1): 6,
        (0, 2): 7, (1, 2): 8, (2, 2): 9,
    }
    directions = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0),
    }

    position = (1, 1)

    if part == '1':
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

    if part == '2':
        click.echo('')


if __name__ == '__main__':
    run()
