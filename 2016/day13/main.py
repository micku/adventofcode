#! /usr/bin/env python

import click
import operator
import itertools

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    fav = int(f.read().strip())

    def around(x, y):
        for pos in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xx = x + pos[0]
            yy = y + pos[1]
            if xx >= 0 and yy >= 0 and '{0:b}'.format(
                fav + (xx*xx + 3*xx + 2*xx*yy + yy + yy*yy)
            ).count('1') % 2 == 0:
                yield (xx, yy) \

    def move(position, target, steps):
        steps.append(position)
        for direction in [x for x in around(*position) if x not in steps]:
            if target == direction:
                yield len(steps) 
            else:
                for ln in move(direction, target, steps[:]):
                    yield ln

    if part == '1':
        starting_point = (1, 1)
        finish_point = (31, 39)
        steps = []
        
        shortest_path = min([x for x in move(starting_point, finish_point, steps)])

    if part == '2':
        pass

    click.echo(shortest_path)


if __name__ == '__main__':
    run()
