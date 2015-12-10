#!python

import click
import re

@click.command()
@click.option('--file', default='day7/input.txt', help='Input file path')
def run(file):
    set_re = re.compile(r'^([0-9a-z]+) -> ([a-z]+)')
    operation_re = re.compile(r'^([a-z0-9]*)[ ]*([A-Z]+) ([a-z0-9]+) -> ([a-z]+)')
    operators = {
        'RSHIFT': '{}>>{}',
        'LSHIFT': '{}<<{}',
        'NOT': '{}~{} & 65535',
        'OR': '{}|{}',
        'AND': '{}&{}',
    }

    wires = {}
    op = []

    with click.open_file(file) as strings:
        for row in strings:
            row = row.rstrip()
            is_set = re.match(set_re, row)
            if is_set is not None:
                # Add biniary conversion
                if is_set.group(1).isdigit():
                    wires[is_set.group(2)] = int(is_set.group(1))
                else:
                    op_data = {
                        'operands': [is_set.group(1), ],
                        'operator': '',
                        'result': is_set.group(2),
                        'source': row,
                        'instruction': 'wires["{}"]'.format(
                            is_set.group(1),
                        )
                    }

                    op.append(op_data)
            else:
                operation = re.match(operation_re, row)
                if operation:
                    op_data = {
                        'operands': filter(None, [operation.group(1), operation.group(3),]),
                        'operator': operation.group(2),
                        'result': operation.group(4),
                        'source': row,
                        'instruction': operators[operation.group(2)].format(
                            '' if operation.group(1) == '' \
                                else operation.group(1) if operation.group(1).isdigit() \
                                else 'wires["{}"]'.format(operation.group(1)),
                            '' if operation.group(3) == '' \
                                else operation.group(3) if operation.group(3).isdigit() \
                                else 'wires["{}"]'.format(operation.group(3)),
                        )
                    }

                    op.append(op_data)


    tot = 0
    while len(op) > 0:
        for instruction in op[:]:
            operands = instruction['operands']
            var_operands = [operand for operand in instruction['operands'] if not operand.isdigit()]
            if len(set(var_operands) & set(wires.keys())) == len(var_operands):
                tot += 1
                wires[instruction['result']] = eval(instruction['instruction'])
                op.remove(instruction)

    click.echo('Evaluated {} instructions'.format(tot))
    click.echo('Wire "a" is {}'.format(wires['a']))


if __name__ == '__main__':
    run()
