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

import click
from asserttool import eprint
from asserttool import ic

from delay_timer import DelayTimer


@click.command()
@click.option('--start', type=float, default=10)
@click.option('--multiplier', type=float, default=0.3)
@click.option('--random', 'random_delay', is_flag=True)
@click.option('--end', type=float, default=359)
@click.option('--verbose', is_flag=True)
def cli(start: float,
        multiplier: float,
        random_delay: bool,
        end: float,
        verbose: bool,
        ):

    if random_delay:
        multiplier = multiplier * random.random()

    delay_timer = DelayTimer(start=start,
                             multiplier=multiplier,
                             end=end,
                             verbose=verbose,)
    ic(delay_timer)
    delay_timer.sleep()

