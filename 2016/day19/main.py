#! /usr/bin/env python

import click
from collections import OrderedDict

@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):
    elves = OrderedDict()
    for e in range(int(f.read().strip())):
        elves[e] = 1

    while len(elves.keys()) > 1:
        elf = elves.popitem(last=False)
        stolen_elf = elves.popitem(last=False)
        elves.update({elf[0]: elf[1]+stolen_elf[1]})
        elves.move_to_end(elf[0], last=True)

    winner = elves.popitem()
    click.echo("Part 1: {}".format(winner[0]+1))


if __name__ == '__main__':
    run()
