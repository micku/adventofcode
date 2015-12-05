#!python

import click
import itertools

@click.command()
@click.option('--file', default='input.txt', help='Input file path')
def run(file):
    with click.open_file(file) as boxes:
        total_paper = 0
        for box in boxes:
            size = [int(s) for s in box.split('x')]
            total_paper += get_box_size(size)

        click.echo('We need {} square feet paper!'.format(total_paper))


def get_box_size(size):
    dimensions = []
    for combo in itertools.combinations(size, 2):
        dimensions.append(combo[0]*combo[1])
    total_size = (sum(dimensions)*2) + min(dimensions)
    return total_size

if __name__ == '__main__':
    run()
