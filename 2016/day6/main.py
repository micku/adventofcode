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
    message = ''
    if part == '1':
        signal = f.read().rstrip().split('\n')
        for position in zip(*signal):
            message += max([{'l': position.count(x), 'c': x} \
                    for x in position], key=lambda y: y['l'])['c']
            

    if part == '2':
        pass

    click.echo(message)


if __name__ == '__main__':
    run()
