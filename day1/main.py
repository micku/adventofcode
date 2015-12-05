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
    index = 0
    basement_position = 0
    with click.open_file(file) as instructions:
        while True:
            where = instructions.read(1)
            if not where:
                click.echo('I was at -1 after {} steps...'.format(basement_position))
                click.echo('{} floor!'.format(floor))
                break
            index += 1
            if where in directions:
                floor += directions[where]
            if not basement_position \
                and floor < 0:
                basement_position = index


if __name__ == '__main__':
    run()
