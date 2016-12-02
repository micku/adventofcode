#! /usr/bin/env python

import click

@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):
    floor = 0
    directions = {
        '(': 1,
        ')': -1,
    }
    index = 0
    basement_position = 0

    route = f.read().rstrip().split(', ')
    print(route)


if __name__ == '__main__':
    run()
