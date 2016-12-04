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
    alphabet = [chr(x) for x in xrange(97, 123)]
    alphabet_start = 97
    alphabet_end = 122

    for room in f:
        m = name_pattern.match(room.strip())
        room_name = m.groups()[0]
        room_id = int(m.groups()[1])
        room_checksum = m.groups()[2]

        cnt = collections.defaultdict(int)
        for l in room_name.replace('-', ''):
            cnt[l] += 1

        calc_checksum = ''.join([
            x[0]
            for x
            in sorted(cnt.iteritems(), key=lambda(k,v): (-v, k))])[:5]

        if part == '1':
            totals += room_id \
                    if room_checksum == calc_checksum \
                    else 0

        if part == '2' and room_checksum == calc_checksum:
            real_name = ''.join([
                    alphabet[(ord(l)-alphabet_start+room_id)%len(alphabet)] \
                            if ord(l) >= alphabet_start \
                            and ord(l) <= alphabet_end \
                            else l
                    for l
                    in room_name.replace('-', ' ')
                    ])
            if 'north' in real_name:
                click.echo('{} - {}'.format(real_name, room_id))

    if part == '1':
        click.echo(totals)


if __name__ == '__main__':
    run()
