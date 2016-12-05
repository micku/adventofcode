#!python

import click
import hashlib

@click.command()
@click.option('--key', default='ckczppom', help='Input key')
def run(key):
    position = 1
    while md5(key+str(position)).startswith('0'*6) == False:
        position += 1
    click.echo('Code is {}'.format(str(position)))


def md5(key):
    m = hashlib.md5()
    m.update(key)

    return m.hexdigest()


if __name__ == '__main__':
    run()
