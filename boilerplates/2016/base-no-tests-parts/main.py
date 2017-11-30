#! /usr/bin/env python

import click
import operator
import itertools

@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):

    click.echo()


if __name__ == '__main__':
    run()
