#! /usr/bin/env python

import unittest

import click
from click.testing import CliRunner
from main import run

class TestAll(unittest.TestCase):
    def test_part1(self):
        tests = [
            ('\n'.join([
                'aaaaa-bbb-z-y-x-123[abxyz]',
                'a-b-c-d-e-f-g-h-987[abcde]',
                'not-a-real-room-404[oarel]',
                'totally-real-room-200[decoy]',
                ], '1514'),
        ]
        self.generic(1, tests)

    def test_part2(self):
        tests = [
            ('', ''),
        ]
        self.generic(2, tests)

    def generic(self, part, tests):
        runner = CliRunner()
        with runner.isolated_filesystem():
            for tst in tests:
                with open('test', 'w') as f:
                    f.write(tst[0])

                result = runner.invoke(run, [str(part), 'test'])
                self.assertEqual(0, result.exit_code)
                self.assertEqual('{}\n'.format(tst[1]), result.output)


if __name__ == '__main__':
    unittest.main()
