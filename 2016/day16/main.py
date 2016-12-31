#! /usr/bin/env python

import click
import operator
import itertools

def generate_data(i, l):
    ret = i
    while len(ret) < l:
        a = ret
        b = a[::-1]
        b = ''.join(['0' if x == '1' else '1' for x in b])
        ret = '{}0{}'.format(a, b)
    return ret

def calc_checksum(data):
    cs = ''
    for x in range(int(len(data) / 2)):
        idx = x * 2
        cs += '1' if data[idx] == data[idx+1] else '0'

    return cs if len(cs) % 2 == 1 else calc_checksum(cs)

@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):
    i = f.read().strip()

    disk_len = [272, 35651584]

    for idx, l in enumerate(disk_len):
        disk_data = generate_data(i, l)
        checksum = calc_checksum(disk_data[:l])

        click.echo('Part {}: {}'.format(idx+1, checksum))


if __name__ == '__main__':
    run()
