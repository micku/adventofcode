#!python

import click
import re
import itertools
import string

@click.command()
@click.option('--value', default='vzbxkghb', help='Input file path')
def run(value):
    dictionary = re.sub(r'(i|o|l)', '', string.ascii_lowercase)
    for val in next_values(value):
        if val == 'ghjaabcc':
            return
        if is_valid(val):
            click.echo('Next password is {}'.format(val))
            break


invalid_chars_re = re.compile(r'(i|o|l)')
double_chars_re = re.compile(r'(.)\1.*(.)\2')
def is_valid(value):
    if re.search(invalid_chars_re, value):
        return False
    if not re.search(double_chars_re, value):
        return False
    for i, x in enumerate(value[:-2]):
        if ord(value[i+1]) == ord(x)+1 and ord(value[i+2]) == ord(x)+2:
            return True
    return False

def next_values(value):
    val = value
    while True:
        strip_zs = val.rstrip('z')
        if strip_zs:
            val = strip_zs[:-1] + chr(ord(strip_zs[-1]) + (1 if strip_zs not in ['i', 'o', 'l'] else 2)) + 'a' * (len(val) - len(strip_zs))
            yield val
        else:
            break

if __name__ == '__main__':
    run()
