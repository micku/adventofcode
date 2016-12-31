#! /usr/bin/env python

import click
import re
import string

output = ''

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    instructions = [l.strip().split(' ') for l in f]

    def get_val(s):
        return int(s) \
                if not s in string.ascii_lowercase \
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

    def out(src):
        global output
        #click.echo('-- out: {}'.format(output))
        output += str(get_val(src))
        return 1

    """
    def tgl(reg, *args):
        i = cnt+get_val(reg)
        if i < len(instructions):
            instructions[i][0] =  repl[instructions[i][0]]
        return 1
    """

    def mul(one, two, dest, *args):
        registers[dest] += get_val(one) * get_val(two)
        return 1

    definitions = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'out': out,
        #'tgl': tgl,
        'mul': mul,
    }

    """
    repl = {
        'cpy': 'jnz',
        'inc': 'dec',
        'dec': 'inc',
        'jnz': 'cpy',
        'out': 'out',
        #'tgl': 'inc',
    }
    """

    if part == '1':
        instructions[1] = ['mul', '170', '15', 'd']
        instructions[2] = ['cpy', '0', 'c']
        instructions[3] = ['cpy', '0', 'c']
        instructions[4] = ['cpy', '0', 'c']
        instructions[5] = ['cpy', '0', 'b']
        instructions[6] = ['cpy', '0', 'b']
        instructions[7] = ['cpy', '0', 'b']

        default_a = 0
        expected_output = '01'*5

    if part == '2':
        registers['a'] = 12


    global output
    while output != expected_output:
        output = ''
        cnt = 0
        registers = {}
        registers['a'] = default_a

        while cnt < len(instructions) and len(output) < 10:
            parsed = instructions[cnt]

            cnt += (definitions[parsed[0]])(*parsed[1:])

        log = "a: {} | out: {} vs. {}".format(
            default_a,
            output,
            expected_output)

        print(log, end='')
        print('\r'*len(log), end='')

        default_a += 1
        
    click.echo()
    click.echo('Day 1: {}'.format(default_a-1))



if __name__ == '__main__':
    run()
