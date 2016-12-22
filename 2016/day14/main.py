#! /usr/bin/env python

import click
import hashlib
import re
from collections import deque

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    keys = []
    salt = f.read().strip()
    idx = -1
    future_keys = deque([])

    is_triplet = re.compile(r'(.)\1\1')
    def calc_key(i):
        hashed = hashlib.md5('{}{}'.format(salt, str(i)).encode('utf-8')).hexdigest()
        if part == '2':
            for _ in range(2016):
                hashed = hashlib.md5(hashed.encode('utf-8')).hexdigest()
        return hashed

    while len(keys) < 64:
        idx += 1

        maybe_key = calc_key(idx) \
            if len(future_keys) == 0 \
            else future_keys.popleft()['key']

        triplet = is_triplet.findall(maybe_key)
        if len(triplet) > 0:
            pattern = triplet[0]
            for quint_idx in range(1, 1001):
                if len(future_keys) >= quint_idx:
                    new_key = future_keys[quint_idx-1]['key']
                else:
                    new_key = calc_key(idx + quint_idx)
                    future_keys.append({'idx': idx + quint_idx, 'key': new_key})
                if pattern*5 in new_key:
                    keys.append({'idx': idx, 'key': maybe_key})
                    break

    click.echo(keys[-1]['idx'])

# wrong: 20141

if __name__ == '__main__':
    run()
