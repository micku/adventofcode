#! /usr/bin/env python

import click
import re
import itertools

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    tls_pwds = 0
    if part == '1':
        for pwd in f:
            tls_pwds += 1 if support_tls(pwd.strip()) else 0

    if part == '2':
        pass

    click.echo(tls_pwds)


r = re.compile('(\[?[a-z]+\]?)')
def support_tls(ip):
    parts = r.findall(ip)
    t = False
    for part in parts:
        if part.startswith('['):
            if is_abba(part[1:-1]):
                return False
        else:
            t |= is_abba(part)

    return t


def is_abba(s):
    for i in xrange(3, len(s)):
        if s[i] == s[i-3] and s[i-1] == s[i-2] and s[i] != s[i-1]:
            return True
    return False



if __name__ == '__main__':
    run()
