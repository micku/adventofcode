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
    idx = 0
    future_keys = deque([])

    is_triplete = re.compile(r'(.)\1\1')
    def calc_key(i):
        return hashlib.md5('{}{}'.format(salt, str(i)).encode('utf-8')).hexdigest()

    if part == '1':
        while len(keys) < 64:
            maybe_key = calc_key(idx) \
                if len(future_keys) == 0 \
                else future_keys.popleft()

            triplete = is_triplete.findall(maybe_key)
            if len(triplete) > 0:
                pattern = triplete[0]
                for quint_idx in range(1, 1000):
                    if len(future_keys) >= quint_idx:
                        new_key = future_keys[quint_idx-1]
                    else:
                        new_key = calc_key(idx + quint_idx)
                        future_keys.append(new_key)
                    if pattern*5 in new_key:
                        keys.append({'idx': idx, 'key': maybe_key})
                        continue
            idx += 1

        click.echo(idx-1)


    if part == '2':
        click.echo()


if __name__ == '__main__':
    run()
