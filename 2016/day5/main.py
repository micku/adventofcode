#! /usr/bin/env python

import click
import itertools
import hashlib

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    door_id = f.read().rstrip()
    password = ''

    def iterate(door_id):
        cnt = 0
        while True:
            md5 = hashlib.md5(
                '{}{}'.format(
                    door_id,
                    str(cnt))).hexdigest()
            if md5[:5] == '0'*5:
                yield md5[5]
            cnt += 1

    def iterate_part2(door_id):
        cnt = 0
        while True:
            md5 = hashlib.md5(
                '{}{}'.format(
                    door_id,
                    str(cnt))).hexdigest()
            if md5[:5] == '0'*5 \
                    and md5[5].isdigit() \
                    and int(md5[5]) < 8:
                yield (int(md5[5]), md5[6])
            cnt += 1

    if part == '1':
        password = ''.join(
                itertools.islice(iterate(door_id), 8))

    if part == '2':
        arr_pwd = [' ']*8
        for char in iterate_part2(door_id):
            arr_pwd[char[0]] = char[1] \
                    if arr_pwd[char[0]] == ' ' \
                    else arr_pwd[char[0]]
            if ' ' not in arr_pwd:
                break
        password = ''.join(arr_pwd)



    click.echo(password)


if __name__ == '__main__':
    run()
