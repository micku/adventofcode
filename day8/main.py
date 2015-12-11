#!python

import click
import re

@click.command()
@click.option('--file', default='day8/input.txt', help='Input file path')
def run(file):
    tot = 0
    tot2 = 0
    with click.open_file(file) as strings:
        for row in strings:
            row = row.rstrip()
            code_len = len(row)
            memory_len = len(eval(row))
            encoded_len = len(row.replace('\\', '\\\\').replace('"', '\\"')) + 2
            tot += code_len - memory_len
            tot2 += encoded_len - code_len

    click.echo('Total is {}'.format(tot))
    click.echo('Total 2 is {}'.format(tot2))


if __name__ == '__main__':
    run()
