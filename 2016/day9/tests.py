#! /usr/bin/env python

import unittest

import click
from click.testing import CliRunner
from main import run

class TestAll(unittest.TestCase):
    def test_part1(self):
        tests = [
            ('ADVENT', '6'),
            ('A(1x5)BC', '7'),
            ('(3x3)XYZ', '9'),
            ('A(2x2)BCD(2x2)EFG', '11'),
            ('(6x1)(1x3)A', '6'),
            ('X(8x2)(3x3)ABCY', '18'),
        ]
        self.generic(1, tests)

    def test_part2(self):
        tests = [
            ('', '0'),
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
