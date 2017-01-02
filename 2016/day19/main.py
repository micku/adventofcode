#! /usr/bin/env python

import click
from collections import deque

@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):
    elves = {}
    s = deque(range(int(f.read().strip())))
    for e in s:
        elves[e] = 1

    while len(s) > 1:
        elf = s.popleft()
        stolen_elf = s.popleft()
        elves[elf] += elves[stolen_elf]
        s.append(elf)

    click.echo("Part 1: {}".format(s[0]+1))


if __name__ == '__main__':
    run()
