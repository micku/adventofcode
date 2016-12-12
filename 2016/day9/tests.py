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
            ('(3x3)XYZ', '9'),
            ('X(8x2)(3x3)ABCY', '20'),
            ('(27x12)(20x12)(13x14)(7x10)(1x12)A', '241920'),
            ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', '445'),
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
