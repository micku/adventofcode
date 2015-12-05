#!python

import click

@click.command()
@click.option('--file', default='input.txt', help='Input file path')
def run(file):
    santas_position = {
        's': [0, 0],
        'r': [0, 0],
    }
    movements = {
        '>': [1, 0],
        '<': [-1, 0],
        '^': [0, -1],
        'v': [0, 1],
    }
    houses = [
        santas_position['s'],
    ]
    active_santa = 's'
    with click.open_file(file) as instructions:
        while True:
            where = instructions.read(1)
            if not where:
                click.echo('We just visited {} houses'.format(len(houses)))
                break
            if where in movements:
                position = santas_position[active_santa]
                position = [sum(i) for i in zip(*[movements[where], position])]
                if position not in houses:
                    houses.append(position)
                santas_position[active_santa] = position
                santas = santas_position.keys()
                santas.remove(active_santa)
                active_santa = santas[0]


if __name__ == '__main__':
    run()
