#!python

import click
import re
import json

@click.command()
@click.option('--file', default='day12/input.txt', help='Input file path')
def run(file):
    num_re = re.compile(r'(-?[0-9]+)')
    js = ''
    with click.open_file(file) as strings:
        for row in strings:
            js += row.rstrip()
    tot = sum([int(x) for x in re.findall(num_re, js)])

    click.echo('Part 1 Total is {}'.format(tot))

    js = json.loads(js)
    tot2 = 0
    for n in parse_block(js):
        tot2 += n
    click.echo('Part 2 Total is {}'.format(tot2))

def parse_block(b):
    if isinstance(b, int):
        yield b
    if isinstance(b, dict):
        for n in parse_dict(b):
            yield n
    if isinstance(b, list):
        for n in parse_list(b):
            yield n

def parse_list(l):
    for e in l:
        for n in parse_block(e):
            yield n

def parse_dict(d):
    if 'red' not in d.values():
        for key in d.keys():
            val = d[key]
            for n in parse_block(val):
                yield n


if __name__ == '__main__':
    run()
