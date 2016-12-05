#!python

import array
import click

@click.command()
@click.option('--file', default='day6/input.txt', help='Input file path')
def run(file):
    table1 = [[False for x in range(1000)] for y in range(1000)]
    table2 = [[0 for x in range(1000)] for y in range(1000)]
    tot = 0
    tot2 = 0
    with click.open_file(file) as strings:
        for row in strings:
            op = row.split(' ')
            if 'turn' in op:
                op.remove('turn')
            instructions = {
                'op': op[0],
                'from': [int(a) for a in op[1].split(',')],
                'to': [int(a) for a in op[3].split(',')],
            }
            for x in range(instructions['from'][0], instructions['to'][0]+1):
                for y in range(instructions['from'][1], instructions['to'][1]+1):
                    val = table1[x][y]
                    val2 = table2[x][y]
                    if instructions['op'] == 'toggle':
                        table1[x][y] = not val
                        tot += 1 if not val else -1
                        table2[x][y] = val2 + 2
                        tot2 += 2
                    if instructions['op'] == 'on':
                        table1[x][y] = True
                        tot += 1 if not val else 0
                        table2[x][y] = val2 + 1
                        tot2 += 1
                    if instructions['op'] == 'off':
                        table1[x][y] = False
                        tot += -1 if val else 0
                        table2[x][y] = val2 + (-1 if val2 else 0)
                        tot2 += -1 if val2 else 0

    click.echo('There are {} lights!'.format(tot))
    click.echo('There are {} lights for step 2!'.format(tot2))


if __name__ == '__main__':
    run()
