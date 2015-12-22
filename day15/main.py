#!python

import click
import re
import json
import itertools

@click.command()
@click.option('--file', default='day15/input.txt', help='Input file path')
def run(file):
    row_re = re.compile(r'([a-zA-Z]+): capacity (-?[0-9]+), durability (-?[0-9]+), flavor (-?[0-9]+), texture (-?[0-9]+), calories (-?[0-9]+)')
    ingredients = []
    with click.open_file(file) as strings:
        for row in strings:
            data = re.match(row_re, row.rstrip())
            #ingredients[data.group(1)] = [
            ingredients.append([
                int(data.group(2)),
                int(data.group(3)),
                int(data.group(4)),
                int(data.group(5)),
                #data.group(6),
            ])
    tot = 0
    for e in loop(1, ingredients, []):
        #for prop in zip(*ingredients):
        temp_tots = []
        for i, v in enumerate(e):
            ing_tots = map(lambda x: x*v, ingredients[i])
            temp_tots.append(ing_tots)
        prop_tots = map(lambda x: sum(list(x)), zip(*temp_tots))
        if min(prop_tots) > 0:
            temp_tot = reduce(lambda k, z: k*z, prop_tots)
            tot = max([tot, temp_tot])

    click.echo('Part 1 Total is {}'.format(tot))

def loop(start, ing, tots):
    if len(ing) == 1:
        yield [100 - sum(tots)]
    else:
        for i in range(1, 100 - (sum(tots))):
            for e in loop(1, ing[1:], tots+[i]):
                yield [i] + e

if __name__ == '__main__':
    run()
