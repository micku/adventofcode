#! /usr/bin/env python

import click


def tile_type(prev):
    return '^' \
            if prev == '^^.' \
            or prev == '.^^' \
            or prev == '^..' \
            or prev == '..^' \
            else '.'


@click.command()
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(f):
    r = f.read().strip()
    
    safe_count = r.count('.')
    
    prev = r
    click.echo(r)
    for i in range(39):
        row = ''
        for i in range(len(prev)):
            row += tile_type(
                '.{}.'.format(prev)[i:i+3]
                )
        safe_count += row.count('.')
        prev = row
        click.echo(row)

    click.echo()
    click.echo(safe_count)


if __name__ == '__main__':
    run()
