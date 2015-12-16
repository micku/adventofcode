#!python

import click
import re
import itertools

@click.command()
@click.option('--file', default='day12/input.txt', help='Input file path')
def run(file):
    num_re = re.compile(r'(-?[0-9]+)')
    js = ''
    with click.open_file(file) as strings:
        for row in strings:
            js += row.rstrip()
    tot = sum([int(x) for x in re.findall(num_re, js)])

    click.echo('Total is {}'.format(tot))


if __name__ == '__main__':
    run()
