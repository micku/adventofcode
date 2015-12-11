#!python

import click
import re

@click.command()
@click.option('--file', default='day8/input.txt', help='Input file path')
def run(file):
    tot = 0
    with click.open_file(file) as strings:
        for row in strings:
            row = row.rstrip()
            tot += len(row) - len(eval(row))

    click.echo('Total is {}'.format(tot))


if __name__ == '__main__':
    run()
