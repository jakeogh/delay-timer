#!/usr/bin/env python3

# pylint: disable=C0111  # docstrings are always outdated and wrong
# pylint: disable=W0511  # todo is encouraged
# pylint: disable=C0301  # line too long
# pylint: disable=R0902  # too many instance attributes
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0103  # single letter var names, func name too descriptive
# pylint: disable=R0911  # too many return statements
# pylint: disable=R0912  # too many branches
# pylint: disable=R0915  # too many statements
# pylint: disable=R0913  # too many arguments
# pylint: disable=R1702  # too many nested blocks
# pylint: disable=R0914  # too many local variables
# pylint: disable=R0903  # too few public methods
# pylint: disable=E1101  # no member for base
# pylint: disable=W0201  # attribute defined outside __init__
# pylint: disable=R0916  # Too many boolean expressions in if statement


import random
import time

import click

try:
    from icecream import ic  # https://github.com/gruns/icecream
except ImportError:
    import sys
    def eprint(*args, **kwargs):
        if 'file' in kwargs.keys():
            kwargs.pop('file')
        print(*args, file=sys.stderr, **kwargs)


class DelayTimer():
    def __init__(self, start, multiplier, end):
        start = float(start)
        multiplier = float(multiplier)
        end = float(end)
        assert start >= 0
        assert end > 0
        assert multiplier > 0
        assert start <= end
        delay = start
        self.delay = delay
        self.multiplier = multiplier
        self.end = end

    def _sleep(self):
        ic(self.delay)
        time.sleep(self.delay)

    def _sleep_next(self):
        if self.delay < self.end:
            self.delay = max(self.delay + (self.delay * self.multiplier), self.end)

    def sleep(self):
        self._sleep()
        self._sleep_next()


@click.command()
@click.argument("paths", type=str, nargs=-1)
@click.option('--start', type=float, default=10)
@click.option('--mutiplier', type=float, default=0.3)
@click.option('--random', 'random_delay', is_flag=True)
@click.option('--end', type=float, default=359)
@click.option('--verbose', is_flag=True)
@click.option('--printn', is_flag=True)
def cli(start,
        multiplier,
        random_delay,
        end,
        verbose,
        printn,):

    null = not printn
    end = '\n'
    if null:
        end = '\x00'
    if sys.stdout.isatty():
        end = '\n'

    if random_delay:
        multiplier = multiplier * random.random()

    delay_timer = DelayTimer(start=start,
                             multiplier=multiplier,
                             end=end,
                             verbose=verbose,)
    ic(delay_timer)
    delay_timer.sleep()

