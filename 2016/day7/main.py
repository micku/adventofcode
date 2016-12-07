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
    ips = 0
    if part == '1':
        for ip in f:
            ips += 1 if support_tls(ip.strip()) else 0

    if part == '2':
        for ip in f:
            ip = ip.strip()
            ips += 1 if support_ssl(ip) else 0

    click.echo(ips)


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


def support_ssl(ip):
    parts = r.findall(ip)
    for aba in find_aba([p for p in parts if not p.startswith('[')]):
        if '{}{}{}'.format(aba[1], aba[0], aba[1]) in find_aba([p[1:-1] for p in parts if p.startswith('[')]):
            return True


def find_aba(a):
    for s in a:
        for i in xrange(2, len(s)):
            if s[i] == s[i-2] and s[i] != s[i-1]:
                yield s[i-2:i+1]



if __name__ == '__main__':
    run()
