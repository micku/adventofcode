#!python

import click
import itertools
import operator
import functools

@click.command()
@click.option('--file', default='input.txt', help='Input file path')
def run(file):
    with click.open_file(file) as boxes:
        total_ribbon = 0
        for box in boxes:
            size = [int(s) for s in box.split('x')]
            box_ribbon = get_bow_size(size) + get_wrap_size(size)
            total_ribbon += box_ribbon

        click.echo('We need {} feet of ribbon!'.format(total_ribbon))


def get_bow_size(size):
    return functools.reduce(operator.mul, size, 1)

def get_wrap_size(size):
    smallest_sides = list(size)
    smallest_sides.remove(max(size))
    return sum(smallest_sides) * 2


if __name__ == '__main__':
    run()
