#! /usr/bin/env python

import click
import itertools
import hashlib

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    door_id = f.read().rstrip()
    password = ''

    def iterate(door_id):
        cnt = 0
        while True:
            md5 = hashlib.md5(
                '{}{}'.format(
                    door_id,
                    str(cnt))).hexdigest()
            if md5[:5] == '0'*5:
                yield md5[5]
            cnt += 1

    if part == '1':
        password = ''.join(
                itertools.islice(iterate(door_id), 8))

    if part == '2':
        pass

    click.echo(password)


if __name__ == '__main__':
    run()
