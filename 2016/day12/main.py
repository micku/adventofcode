#! /usr/bin/env python

import click
import re

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    instructions = [l.strip() for l in f]
    registers = {}
    cnt = 0
    parser = re.compile(r'^([a-z]+) ([a-z0-9]+) ?([a-z0-9\-]+)?')

    def get_val(s):
        def isint(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False

        return int(s) \
                if isint(s) \
                else \
                    registers[s] \
                    if s in registers \
                    else None

    def cpy(src, dest):
        registers[dest] = get_val(src) or 0
        return 1

    def inc(reg, *args):
        pre = registers[reg]
        registers[reg] += 1
        return 1

    def dec(reg, *args):
        pre = registers[reg]
        registers[reg] -= 1
        return 1

    def jnz(reg, step):

        ret = get_val(step) \
                if get_val(reg) is not None and get_val(reg) > 0 \
                else 1
        return ret

    definitions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
    }

    if part == '1':
        while cnt < len(instructions):
            parsed = list(parser.search(instructions[cnt]).groups())

            cnt += (definitions[parsed[0]])(*parsed[1:])
            
        click.echo(registers['a'])

    if part == '2':
        click.echo()



if __name__ == '__main__':
    run()
