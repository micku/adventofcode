#!python

import click
import re
import json
import itertools

@click.command()
@click.option('--file', default='day14/input.txt', help='Input file path')
def run(file):
    row_re = re.compile(r'([a-zA-Z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.*')
    caribou_list = {}
    with click.open_file(file) as strings:
        for row in strings:
            data = re.match(row_re, row.rstrip())
            caribou_list[data.group(1)] = [
                int(data.group(2)),
                int(data.group(3)),
                int(data.group(4)),
            ]
    max_time = 2503
    totals = []
    for k, v in caribou_list.iteritems():
        totals.append(
            ((max_time / (v[1]+v[2])) * (v[1]*v[0])) + \
                min([v[1], (max_time % (v[1]+v[2]))]) * v[0]
        )

    click.echo('Part 1 Total is {}'.format(max(totals)))

if __name__ == '__main__':
    run()
