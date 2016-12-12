#! /usr/bin/env python

import click
import operator
import string

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    out = expand(f.read(), part)

    click.echo(out)


def expand(s, part):
    ret = 0

    length = '0'
    repetitions = '0'
    text = ''
    counter = 0

    repeting = False
    marker = False
    markerx = False

    for c in s:
        if not marker and not markerx and int(length) == 1:
            length = '0'
            text += c


            if part == '1':
                ret += len(text) * int(repetitions)

            if part == '2':
                ret += expand(text, part) * int(repetitions)
            text = ''
            repetitions = '0'

            continue

        if not marker and not markerx and int(length) > 1:
            length = str(int(length)-1)
            text += c
            continue

        if not marker and not markerx and c == '(' and int(length) == 0:
            marker = True
            continue

        if marker and not markerx and c in string.digits:
            length += c
            continue

        if marker and not markerx and c == 'x':
            markerx = True
            continue

        if marker and markerx and c in string.digits:
            repetitions += c
            continue

        if marker and markerx and c == ')':
            marker = False
            markerx = False
            continue

        ret += len(c.strip())
    return ret



if __name__ == '__main__':
    run()
