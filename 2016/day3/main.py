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
    possible = 0
    if part == '1':
        for triangle in f:
            sides = [
                int(triangle[:5]),
                int(triangle[5:10]),
                int(triangle[10:])]
            possible += 1 \
                if all([True if sum(combination[:2]) > combination[2] else False 
                    for combination in itertools.permutations(sides)]) \
                else 0

    if part == '2':
        idx = 0
        sides = []
        for triangle in f:
            idx += 1
            sides.append([
                int(triangle[:5]),
                int(triangle[5:10]),
                int(triangle[10:])])
            if idx%3 == 0:
                z = zip(*sides[idx-3:idx])
                for t in z:
                    possible += 1 \
                        if all([True if sum(combination[:2]) > combination[2] else False 
                            for combination in itertools.permutations(t)]) \
                        else 0

    click.echo(possible)


if __name__ == '__main__':
    run()
