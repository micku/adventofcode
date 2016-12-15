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
    outputs = []

    pending_bots, ready_bots, outputs = solve(f, pending_bots, ready_bots, outputs)
    
    zot = [x['values'][0] for x in outputs if x['id'] in [0, 1, 2]]
    click.echo(zot[0]*zot[1]*zot[2])


def solve(instructions, pending_bots, ready_bots, outputs):
    def parse(instruction):
        who, low, high = map(int,re.findall(r'-?\d+', instruction))
        return {
            'id': who,
            'min': low,
            'max': high
        }

    def assign(t_id, val, is_bot):
        if is_bot:
            is_pending = filter(lambda x: x['id'] == t_id, pending_bots)
            if is_pending:
                bot = is_pending[0]
                pending_bots.remove(bot)
                bot['values'].append(val)
                ready_bots.append(bot)
                if set(bot['values']).issuperset([17, 61]):
                    print bot['id']
            else:
                bot = {
                    'id': t_id,
                    'values': [val, ]
                }
                pending_bots.append(bot)
            return bot
        else:
            is_pending = filter(lambda x: x['id'] == t_id, outputs)
            if is_pending:
                output = is_pending[0]
                is_pending[0]['values'].append(val)
            else:
                output = {
                    'id': t_id,
                    'values': [val, ]
                }
                outputs.append(output)
            return output

    next_instructions = []
    for instruction in instructions:
        if instruction.startswith('value'):
            val, who = map(int,re.findall(r'-?\d+', instruction))
            assign(who, val, True)
        else:
            i = parse(instruction)
            is_ready = filter(lambda x: x['id'] == i['id'], ready_bots)
            if is_ready:
                bot_out = re.findall(r' (bot|output)', instruction)
                assign(i['min'], min(is_ready[0]['values']), bot_out[0] == 'bot')
                assign(i['max'], max(is_ready[0]['values']), bot_out[1] == 'bot')
            else:
                next_instructions.append(instruction)
    return solve(next_instructions, pending_bots, ready_bots, outputs) \
            if next_instructions \
            else pending_bots, ready_bots, outputs



if __name__ == '__main__':
    run()
