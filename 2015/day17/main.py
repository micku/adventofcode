#! /usr/bin/env python

import click
import itertools

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    possible = 0
    
    if part == '1':
        sizes = [int(x)
                for x
                in f.read().rstrip().split('\n')]
        for i in xrange(2, len(sizes)):
            for perm in itertools.combinations(sizes, i):
                possible += 1 if sum(perm) == 150 else 0

    if part == '2':
        pass

    click.echo(possible)


if __name__ == '__main__':
    run()
