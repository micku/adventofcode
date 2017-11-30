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
    if part == '1':
        pass

    if part == '2':
        pass

    click.echo()


if __name__ == '__main__':
    run()
