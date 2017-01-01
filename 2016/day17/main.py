#! /usr/bin/env python

import click
import hashlib
from collections import deque


def calc_doors_state(s):
    return hashlib.md5(s.encode('utf8')).hexdigest()[:4]


def is_open(s):
    return s in 'bcdef'


def get_directions(passcode, current, possible_directions):
    states = calc_doors_state(passcode+current[0])
    for i in range(len(possible_directions['order'])):
        direction = possible_directions['order'][i]
        coord_s = possible_directions[direction]
        if current[1][0] + coord_s[0] in range(4) \
                and current[1][1] + coord_s[1] in range(4) \
                and is_open(states[i]):
            yield (direction, (current[1][0] + coord_s[0], current[1][1] + coord_s[1]))


@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):
    passcode = f.read().strip()
    start_coord = (0, 0)
    end_coord = (3, 3)
    path = ''

    directions = {
        'order': 'UDLR',
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    start = ('', start_coord)
    q = deque()
    q.append(start)

    all_paths = set([])

    while q:
        current = q.popleft()

        if current[1] == end_coord:
            all_paths.add(current[0])
            continue

        for direction in get_directions(passcode, current, directions):
            q.append((current[0]+direction[0], direction[1]))

    click.echo('Day 1: {}'.format(min(all_paths, key=lambda x:len(x))))
    click.echo('Day 2: {}'.format(len(max(all_paths, key=lambda x:len(x)))))


if __name__ == '__main__':
    run()
