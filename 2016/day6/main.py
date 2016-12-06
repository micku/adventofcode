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
    click.echo(''.join([
        (max if part == '1' else min) \
            ([{'l': position.count(x), 'c': x} \
            for x in position], key=lambda y: y['l'])['c']
        for position in zip(*f.read().rstrip().split('\n'))]))


if __name__ == '__main__':
    run()


"""
Bonus: one line
print(', '.join([''.join([(func)([{'l': position.count(x), 'c': x} for x in position], key=lambda y: y['l'])['c'] for position in zip(*open('input.txt', 'r').read().rstrip().split('\n'))]) for func in [max, min]]))
"""
