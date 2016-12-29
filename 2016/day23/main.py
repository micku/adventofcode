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
    instructions = [l.strip().split(' ') for l in f]
    registers = {}
    cnt = 0

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
            registers[reg] += 1
            return 1

    def dec(reg, *args):
            registers[reg] -= 1
            return 1

    def jnz(reg, step):
            ret = get_val(step) \
                    if get_val(reg) is not None and get_val(reg) != 0 \
                    else 1
            return ret

    def tgl(reg, *args):
        i = cnt+get_val(reg)
        if i < len(instructions):
            instructions[i][0] =  repl[instructions[i][0]]
        return 1

    def mul(one, two, dest, *args):
        registers[dest] += get_val(one) * get_val(two)
        return 1

    definitions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'tgl': tgl,
        'mul': mul,
    }

    repl = {
        'cpy': 'jnz',
        'inc': 'dec',
        'dec': 'inc',
        'jnz': 'cpy',
        'tgl': 'inc',
    }

    if part == '1':
        registers['a'] = 7

    if part == '2':
        registers['a'] = 12

        instructions[4] = ['mul', 'b', 'd', 'a']
        instructions[5] = ['cpy', '0', 'c']
        instructions[6] = ['cpy', '0', 'c']
        instructions[7] = ['cpy', '0', 'd']
        instructions[8] = ['cpy', '0', 'd']
        instructions[9] = ['cpy', '0', 'd']



    while cnt < len(instructions):
        parsed = instructions[cnt]

        cnt += (definitions[parsed[0]])(*parsed[1:])
        
    click.echo(registers['a'])



if __name__ == '__main__':
    run()
