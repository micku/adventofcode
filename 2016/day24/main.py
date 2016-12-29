#! /usr/bin/env python

import click
import string
from collections import deque
import itertools
import sys
import functools

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    free = []
    checkpoints = []
    start = None

    ln = 0
    for l in f:
        cn = 0
        for c in l:
            coord = (cn, ln)
            if c == '0':
                start = coord
                free.append(coord)
            elif c in string.digits[1:]:
                checkpoints.append(coord)
                free.append(coord)
            elif c == '.':
                free.append(coord)
            cn += 1
        ln += 1


    def around(x, y):
        for pos in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xx = x + pos[0]
            yy = y + pos[1]
            if xx >= 0 and yy >= 0 and (xx, yy) in free:
                yield (xx, yy)

    
    memo = {}
    def search_checkpoint(start, checkpoint):
        if (start, checkpoint) in memo.keys():
            return memo[(start, checkpoint)]
        q = deque()
        q.append({
            'pos': start,
            'distance': 0,
            'parent': None
        })
        visited = [start]

        while q:
            current = q.popleft()
            if current['pos'] == checkpoint:
                memo[(start, checkpoint)] = (current['distance'], current['pos'])
                return (current['distance'], current['pos'])

            for n in [x for x in around(*current['pos']) \
                    if x not in visited]:
                visited.append(n)
                new_point = {
                    'pos': n,
                    'distance': current['distance'] + 1,
                    'parent': current
                }
                q.append(new_point)


    distances = []
    record = sys.maxsize
    if part == '1':
        for path in itertools.permutations(checkpoints):
            current = start
            q = deque(path)
            l = 0
            while q:
                c = q.popleft()
                distance, point = search_checkpoint(current, c)
                l += distance
                current = point
                if l >= record:
                    break
            distances.append(l)
            record = min([record, l])


    if part == '2':
        pass

    click.echo(record)


if __name__ == '__main__':
    run()
