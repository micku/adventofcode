#! /usr/bin/env python

import click
import re

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    discs = []

    in_re = re.compile(r'')
    for r in f:
        b, c, _, e = [int(x) for x in re.findall(r'[0-9]+', r)]
        discs.append({'id': b, 'size': c, 'position': e})

    def calc_pos(disc, i):
        return (disc['position'] +disc['id'] + i) % disc['size']

    idx = 0
    if part == '1':
        while not all([calc_pos(x, idx)==0 for x in discs]):
            idx += 1

    if part == '2':
        pass

    click.echo(idx)


if __name__ == '__main__':
    run()
