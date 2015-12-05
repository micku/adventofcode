#!python

import click

@click.command()
@click.option('--file', default='day5/input.txt', help='Input file path')
def run(file):
    nice_strings = 0
    with click.open_file(file) as strings:
        for row in strings:
            if has_doubles(row) \
                and enough_vowels(row) \
                and not poor_strings(row):
                nice_strings += 1
    click.echo('Found {} nice strings'.format(nice_strings))


def has_doubles(string):
    for i in xrange(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False


def enough_vowels(string):
    total_vowels = 0
    for vowel in 'aeiou':
        total_vowels += string.count(vowel)
    return total_vowels >= 3


def poor_strings(string):
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in string:
            return True
    return False


if __name__ == '__main__':
    run()
