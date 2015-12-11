#!python

import click
import re
import itertools
import collections

@click.command()
@click.option('--value', default='1113222113', help='Input file path')
@click.option('--iterations', default='40', help='Input file path')
def run(value, iterations):
    iterations = int(iterations)
    for i in range(iterations):
        value = calc(value)

    click.echo('Final value: {}'.format(value))
    click.echo('Final len: {}'.format(len(value)))


def calc(value):
    ret = []
    for s in value:
        if len(ret) == 0 or ret[-1] != s:
            ret.append(1)
            ret.append(s)
        else:
            ret[-2] += 1
    return ''.join([str(x) for x in ret])

if __name__ == '__main__':
    run()
