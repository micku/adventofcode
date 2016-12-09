#! /usr/bin/env python

import click
import re
import itertools

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    #screen = [[False]*7 for i in xrange(3)]
    screen = [[False]*50 for i in xrange(6)]

    def rect(x, y, s):
        for l in xrange(x):
            for w in xrange(y):
                s[w][l] = True
        return s

    def rotate_row(y, n, s):
        s[y] = s[y][-n:] + s[y][:-n]
        return s

    def rotate_column(x, n, s):
        rot = rotate_row(x, n, zip(*s))
        return [list(x) for x in zip(*rot)]

    rx = re.compile(r'(rotate (row|column)|rect) ([xy]?=?(\d*)(( by )|(x))(\d*))')
    if part == '1':
        for instruction in f:
            parsed = rx.search(instruction).groups()
            func = parsed[0].replace(' ', '_')
            par1 = int(parsed[3])
            par2 = int(parsed[7])
            screen = eval('{}({}, {}, {})'.format(
                func,
                par1,
                par2,
                screen))

    if part == '2':
        pass

    click.echo(sum([l.count(True) for l in screen]))
    for x in screen:
        print ''.join(['#' if e else '.' for e in x])


if __name__ == '__main__':
    run()
