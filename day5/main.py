#!python

import click

@click.command()
@click.option('--file', default='day5/input.txt', help='Input file path')
def run(file):
    nice_strings = 0
    with click.open_file(file) as strings:
        for row in strings:
            if has_repeats(row) \
                and enough_double_doubles(row):
                nice_strings += 1
    click.echo('Found {} nice strings'.format(nice_strings))


def has_repeats(string):
    for i in xrange(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


def enough_double_doubles(string):
    for i in xrange(len(string)-3):
        double = string[i:i+2]
        if double in string.replace(double, ' ', 1):
            return True
    return False


if __name__ == '__main__':
    run()
