#!python

import click
import re
import json
import itertools

@click.command()
@click.option('--file', default='day13/input.txt', help='Input file path')
def run(file):
    row_re = re.compile(r'([a-zA-Z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+).*')
    happiness = {}
    with click.open_file(file) as strings:
        for row in strings:
            data = re.match(row_re, row.rstrip())
            if data.group(1) not in happiness:
                happiness[data.group(1)] = {}
            happiness[data.group(1)][data.group(4)] = int(
                    ('' if data.group(2) == 'gain' else '-') + data.group(3))
    me = {}
    for per in happiness.keys():
        happiness[per]['me'] = 0
        me[per] = 0
    happiness['me'] = me

    tots = []
    for p in itertools.permutations(happiness.keys()):
        l = list(p)
        tot = sum([happiness[l[i]][l[i-1]] + happiness[l[i]][l[(i+1)%len(l)]] for i, k in enumerate(l)])
        tots.append(tot)

    click.echo('Part 2 Total is {}'.format(max(tots)))

if __name__ == '__main__':
    run()
