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
    free = set()
    checkpoints = set()
    start = None

    ln = 0
    for l in f:
        cn = 0
        for c in l:
            coord = (cn, ln)
            if c == '0':
                start = coord
                free.add(coord)
            elif c in string.digits[1:]:
                checkpoints.add(coord)
                free.add(coord)
            elif c == '.':
                free.add(coord)
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
        q.append((
            start,
            0,
            ))
        visited = set(start)

        while q:
            current = q.popleft()
            if current[0] == checkpoint:
                memo[(start, checkpoint)] = (current[1], current[0])
                return (current[1], current[0])

            for n in [x for x in around(*current[0]) \
                    if x not in visited]:
                visited.add(n)
                new_point = (
                        n,
                        current[1] + 1,
                        )
                q.append(new_point)


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
            record = min([record, l])


    if part == '2':
        for path in itertools.permutations(checkpoints):
            current = start
            q = deque(path)
            q.append(start)
            l = 0
            while q:
                c = q.popleft()
                distance, point = search_checkpoint(current, c)
                l += distance
                current = point
                if l >= record:
                    break
            record = min([record, l])

    click.echo(record)


if __name__ == '__main__':
    run()
