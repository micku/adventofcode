#! /usr/bin/env python

import click
import re
import collections

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    name_pattern = re.compile('^([a-z\-]+)-([0-9]+)\[([a-z]+)\]$')
    totals = 0

    if part == '1':
        for room in f:
            m = name_pattern.match(room.strip())
            room_name = m.groups()[0].replace('-', '')
            room_id = int(m.groups()[1])
            room_checksum = m.groups()[2]

            cnt = collections.defaultdict(int)
            for l in room_name:
                cnt[l] += 1

            calc_checksum = ''.join([
                x[0]
                for x
                in sorted(cnt.iteritems(), key=lambda(k,v): (-v, k))])[:5]

            totals += room_id \
                    if room_checksum == calc_checksum \
                    else 0

    if part == '2':
        pass

    click.echo(totals)


if __name__ == '__main__':
    run()
