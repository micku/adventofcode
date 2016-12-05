#!python

import click
import re
import json
import itertools

@click.command()
@click.option('--file', default='day16/input.txt', help='Input file path')
def run(file):
    row_re = re.compile(r'Sue ([0-9]+): (.*)')
    compounds_list = [
        'children',
        'cats',
        'samoyeds',
        'pomeranians',
        'akitas',
        'vizslas',
        'goldfish',
        'trees',
        'cars',
        'perfumes',
    ]
    package_compounds = {
        'children': '3',
        'cats': '7',
        'samoyeds': '2',
        'pomeranians': '3',
        'akitas': '0',
        'vizslas': '0',
        'goldfish': '5',
        'trees': '3',
        'cars': '2',
        'perfumes': '1',
    }
    real_sue = 0
    real_sue_score = 0
    real_sue2 = 0
    real_sue_score2 = 0
    with click.open_file(file) as strings:
        for row in strings:
            data = re.match(row_re, row.rstrip())
            sue_n = data.group(1)

            compounds = [x.split(': ') for x in data.group(2).split(', ')]

            score = len([x for x in compounds if x[1] == package_compounds[x[0]]])
            score2 = len([x for x in compounds if mfcsam(x, package_compounds[x[0]])])
            
            if score > real_sue_score:
                real_sue_score = score
                real_sue = sue_n
            
            if score2 > real_sue_score2:
                real_sue_score2 = score2
                real_sue2 = sue_n

    click.echo('Part 1 Sue is {}'.format(real_sue))
    click.echo('Part 2 Sue is {}'.format(real_sue2))


def mfcsam(x, y):
    if x[0] in ['cats', 'trees']:
        return x[1] > y
    if x[0] in ['pomeranians', 'goldfish']:
        return x[1] < y
    else:
        return x[1] == y

if __name__ == '__main__':
    run()
