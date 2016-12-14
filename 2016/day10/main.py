#! /usr/bin/env python

import click
import operator
import re

@click.command()
@click.argument('part',
        default='1')
@click.argument('f',
        type=click.File(),
        default='input.txt')
def run(part, f):
    pending_bots = []
    ready_bots = []

    if part == '1':
        solve(f, pending_bots, ready_bots)

    if part == '2':
        pass

    click.echo()


def solve(instructions, pending_bots, ready_bots):
    def parse(instruction):
        who, low, high = map(int,re.findall(r'-?\d+', instruction))
        return {
            'id': who,
            'min': low,
            'max': high
        }

    def assign(bot_id, val):
        is_pending = filter(lambda x: x['id'] == bot_id, pending_bots)
        if is_pending:
            bot = is_pending[0]
            pending_bots.remove(bot)
            bot['values'].append(val)
            ready_bots.append(bot)
            if set(bot['values']).issuperset([17, 61]):
                print bot['id']
        else:
            bot = {
                'id': bot_id,
                'values': [val, ]
            }
            pending_bots.append(bot)
        return bot

    next_instructions = []
    for instruction in instructions:
        if instruction.startswith('value'):
            val, who = map(int,re.findall(r'-?\d+', instruction))
            assign(who, val)
        else:
            i = parse(instruction)
            is_ready = filter(lambda x: x['id'] == i['id'], ready_bots)
            if is_ready:
                assign(i['min'], min(is_ready[0]['values']))
                assign(i['max'], max(is_ready[0]['values']))
            else:
                next_instructions.append(instruction)
    return solve(next_instructions, pending_bots, ready_bots) \
            if next_instructions \
            else pending_bots, ready_bots



if __name__ == '__main__':
    run()
