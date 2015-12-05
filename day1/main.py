#!python

import click

@click.command()
@click.option('--file', default='input.txt', help='Input file path')
def run(file):
    floor = 0
    directions = {
        '(': 1,
        ')': -1,
    }
    with click.open_file(file) as instructions:
        while True:
            where = instructions.read(1)
            if not where:
                click.echo('{} floor!'.format(floor))
                break
            if where in directions:
                floor += directions[where]

if __name__ == '__main__':
    run()
